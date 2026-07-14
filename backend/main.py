from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tempfile, os, uuid, subprocess, shutil, time, glob

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB — suficiente para a maioria das plantas
FILE_TTL_SECONDS = 60 * 60  # PDFs gerados expiram depois de 1 hora

def cleanup_old_pdfs():
    """Remove PDFs gerados há mais de FILE_TTL_SECONDS para não acumular no disco."""
    now = time.time()
    for path in glob.glob("/tmp/*.pdf"):
        try:
            if now - os.path.getmtime(path) > FILE_TTL_SECONDS:
                os.remove(path)
        except OSError:
            pass

PAPER_SIZES = {
    "A4":  (210, 297),
    "A3":  (297, 420),
    "A2":  (420, 594),
    "A1":  (594, 841),
    "A0":  (841, 1189),
    "Letter": (215.9, 279.4),
}

DWG2DXF = shutil.which("dwg2dxf")  # None se não instalado

def dwg_to_dxf(dwg_path: str) -> str:
    """Converte DWG → DXF usando libredwg. Retorna caminho do DXF."""
    if not DWG2DXF:
        raise HTTPException(
            422,
            "Conversão automática de DWG não está disponível neste servidor. "
            "Por favor, converta para DXF antes do upload usando QCAD ou LibreCAD (ambos gratuitos). "
            "Dica: no AutoCAD, use 'Salvar uma cópia' → formato DXF."
        )
    out_dir = tempfile.mkdtemp()
    result = subprocess.run(
        [DWG2DXF, "--minimal", "-o", out_dir, dwg_path],
        capture_output=True, text=True, timeout=60
    )
    # dwg2dxf cria o arquivo com o mesmo nome mas extensão .dxf
    base = os.path.splitext(os.path.basename(dwg_path))[0]
    dxf_path = os.path.join(out_dir, base + ".dxf")
    if not os.path.exists(dxf_path):
        raise HTTPException(
            422,
            f"Falha ao converter o DWG: o arquivo pode estar corrompido ou em versão não suportada. "
            f"Detalhe: {result.stderr[:300] if result.stderr else 'sem detalhes'}"
        )
    return dxf_path

@app.get("/api/options")
def get_options():
    return {
        "paper_sizes": list(PAPER_SIZES.keys()),
        "dwg_supported": DWG2DXF is not None,
    }

@app.post("/api/convert")
async def convert(
    file: UploadFile = File(...),
    scale: str = Form("auto"),
    paper: str = Form("A4"),
    orientation: str = Form("auto"),
):
    ext = os.path.splitext(file.filename or "")[-1].lower()
    if ext not in (".dxf", ".dwg"):
        raise HTTPException(400, "Formato inválido. Envie um arquivo .dxf ou .dwg")

    cleanup_old_pdfs()

    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(413, f"Arquivo muito grande. Limite atual: {MAX_FILE_SIZE // (1024*1024)} MB.")

    # Salva o arquivo enviado
    with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    dxf_path = tmp_path
    tmp_dxf_dir = None

    try:
        # Se for DWG, converte para DXF primeiro
        if ext == ".dwg":
            converted = dwg_to_dxf(tmp_path)
            dxf_path = converted
            tmp_dxf_dir = os.path.dirname(converted)

        # Lê e renderiza o DXF
        doc = ezdxf.readfile(dxf_path)
        msp = doc.modelspace()

        fig = plt.figure()
        ax  = fig.add_axes([0, 0, 1, 1])
        ctx = RenderContext(doc)
        out = MatplotlibBackend(ax)
        Frontend(ctx, out).draw_layout(msp, finalize=True)

        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        draw_w = xmax - xmin
        draw_h = ymax - ymin

        if draw_w <= 0 or draw_h <= 0:
            raise HTTPException(422, "O arquivo parece estar vazio ou sem geometria visível.")

        pw_mm, ph_mm = PAPER_SIZES.get(paper, (210, 297))

        if orientation == "auto":
            landscape = (draw_w / draw_h) > (pw_mm / ph_mm)
        else:
            landscape = orientation == "landscape"

        if landscape:
            pw_mm, ph_mm = ph_mm, pw_mm

        margin_mm = 10
        usable_w  = pw_mm - 2 * margin_mm
        usable_h  = ph_mm - 2 * margin_mm

        if scale == "auto":
            scale_factor = min(usable_w / draw_w, usable_h / draw_h)
        else:
            parts = scale.split(":")
            num, den = float(parts[0]), float(parts[1])
            scale_factor = den / num
            # Cap para não sair do papel
            scale_factor = min(scale_factor, usable_w / draw_w, usable_h / draw_h)

        fig_w_mm = min(draw_w * scale_factor + 2 * margin_mm, pw_mm)
        fig_h_mm = min(draw_h * scale_factor + 2 * margin_mm, ph_mm)

        fig.set_size_inches(fig_w_mm / 25.4, fig_h_mm / 25.4)
        ax.set_aspect("equal")
        ax.axis("off")

        out_id  = str(uuid.uuid4())
        out_pdf = f"/tmp/{out_id}.pdf"
        fig.savefig(out_pdf, format="pdf", dpi=300, bbox_inches="tight",
                    pad_inches=margin_mm / 25.4)
        plt.close(fig)

        # Calcula escala real usada
        if scale == "auto":
            if scale_factor >= 1:
                scale_str = f"{scale_factor:.2f}:1"
            else:
                scale_str = f"1:{1/scale_factor:.0f}"
        else:
            scale_str = scale

        orient_str = "Paisagem" if landscape else "Retrato"

        return {
            "file_id": out_id,
            "download_url": f"/api/download/{out_id}",
            "info": {
                "escala": scale_str,
                "papel": f"{paper} · {orient_str}",
                "dimensoes": f"{pw_mm:.0f} × {ph_mm:.0f} mm",
                "origem": "DWG → DXF → PDF" if ext == ".dwg" else "DXF → PDF",
            }
        }

    except ezdxf.DXFError as e:
        raise HTTPException(422, f"Erro ao ler o DXF: {str(e)}")
    finally:
        os.unlink(tmp_path)
        if tmp_dxf_dir:
            shutil.rmtree(tmp_dxf_dir, ignore_errors=True)

@app.get("/api/download/{file_id}")
def download(file_id: str):
    if not file_id.replace("-", "").isalnum():
        raise HTTPException(400, "ID inválido")
    path = f"/tmp/{file_id}.pdf"
    if not os.path.exists(path):
        raise HTTPException(404, "Arquivo não encontrado ou expirado")
    return FileResponse(path, media_type="application/pdf",
                        filename="desenho_exportado.pdf")

app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")
