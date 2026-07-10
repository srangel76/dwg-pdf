# DXF → PDF Converter

Converte arquivos DXF (CAD) para PDF com escala controlada.

## Stack
- **Backend**: Python + FastAPI + ezdxf + matplotlib
- **Frontend**: HTML/JS puro (servido pelo próprio FastAPI)

## Rodando localmente

```bash
pip install -r backend/requirements.txt
cd backend
uvicorn main:app --reload
# Acesse: http://localhost:8000
```

## Deploy no Railway

1. Crie um projeto no [railway.app](https://railway.app)
2. Conecte este repositório GitHub
3. O Railway detecta o `Procfile` automaticamente
4. Pronto — URL pública gerada em ~2 minutos

## Deploy no Render

1. Crie um **Web Service** no [render.com](https://render.com)
2. Conecte o repositório
3. **Build command**: `pip install -r backend/requirements.txt`
4. **Start command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

## Sobre DWG vs DXF

DWG é proprietário da Autodesk. Este conversor aceita **DXF**, que é o formato aberto equivalente. Para converter:
- **QCAD** (gratuito) → Abrir DWG → Salvar como DXF
- **LibreCAD** (gratuito)
- **AutoCAD** → Salvar uma cópia → DXF

## Estrutura

```
dwg-converter/
├── backend/
│   ├── main.py          # API FastAPI
│   └── requirements.txt
├── frontend/
│   └── index.html       # Interface web
├── Procfile             # Deploy Railway/Render
└── README.md
```
