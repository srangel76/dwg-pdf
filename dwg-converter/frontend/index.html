<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>DWG/DXF → PDF · Conversor de Plantas e Projetos</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --blue-50: #E6F1FB; --blue-200: #85B7EB; --blue-600: #185FA5; --blue-800: #0C447C;
  --gray-50: #F1EFE8; --gray-100: #D3D1C7; --gray-400: #888780; --gray-700: #444441; --gray-900: #2C2C2A;
  --teal-50: #E1F5EE; --teal-200: #5DCAA5; --teal-600: #0F6E56; --teal-800: #085041;
  --coral-50: #FAECE7; --coral-200: #F0997B; --coral-600: #993C1D;
  --green-50: #EAF3DE; --green-200: #97C459; --green-600: #3B6D11; --green-800: #27500A;
  --amber-50: #FAEEDA; --amber-600: #854F0B;
  --surface: #FAFAF8;
  --radius: 8px;
}
body { background: var(--surface); color: var(--gray-900); min-height: 100vh; font-family: 'Inter', system-ui, sans-serif; }

header {
  border-bottom: 1px solid var(--gray-100); padding: 0 2rem; height: 60px;
  display: flex; align-items: center; justify-content: space-between;
  background: #fff; position: sticky; top: 0; z-index: 10;
}
.logo { display: flex; align-items: center; gap: 10px; font-weight: 600; font-size: 15px; }
.logo-icon {
  width: 32px; height: 32px; background: var(--blue-600);
  border-radius: 8px; display: flex; align-items: center; justify-content: center;
}
.logo-icon svg { width: 18px; height: 18px; fill: none; stroke: #fff; stroke-width: 1.8; }
.badge {
  font-size: 11px; font-weight: 500; padding: 3px 10px;
  background: var(--teal-50); color: var(--teal-600);
  border-radius: 20px; border: 1px solid var(--teal-200);
}

main { max-width: 760px; margin: 0 auto; padding: 3rem 1.5rem 5rem; }

.hero { text-align: center; margin-bottom: 2.5rem; }
.hero h1 { font-size: 2rem; font-weight: 600; line-height: 1.25; margin-bottom: .75rem; }
.hero p { font-size: 1rem; color: var(--gray-400); max-width: 480px; margin: 0 auto; }

.formats {
  display: flex; justify-content: center; gap: 8px; margin-top: 1rem;
}
.fmt-pill {
  font-size: 12px; font-weight: 500; padding: 4px 14px;
  border-radius: 20px; font-family: 'JetBrains Mono', monospace;
}
.fmt-dwg { background: var(--teal-50); color: var(--teal-600); border: 1px solid var(--teal-200); }
.fmt-dxf { background: var(--blue-50); color: var(--blue-600); border: 1px solid var(--blue-200); }
.fmt-arrow { color: var(--gray-400); font-size: 14px; display: flex; align-items: center; }

.card {
  background: #fff; border: 1px solid var(--gray-100);
  border-radius: 16px; padding: 2rem; margin-bottom: 1rem;
}
.card-title {
  font-size: 11px; font-weight: 500; color: var(--gray-400);
  text-transform: uppercase; letter-spacing: .07em; margin-bottom: 1.25rem;
}

#dropzone {
  border: 2px dashed var(--gray-100); border-radius: 12px;
  padding: 3rem 2rem; text-align: center; cursor: pointer;
  transition: border-color .2s, background .2s;
}
#dropzone:hover, #dropzone.drag { border-color: var(--blue-200); background: var(--blue-50); }
#dropzone input { display: none; }
.drop-icon { margin: 0 auto 1rem; color: var(--blue-200); width: 48px; height: 48px; }
.drop-icon svg { width: 100%; height: 100%; }
#dropzone h3 { font-size: 15px; font-weight: 500; margin-bottom: .35rem; }
#dropzone p  { font-size: 13px; color: var(--gray-400); }

.file-selected {
  display: flex; align-items: center; gap: 12px;
  background: var(--blue-50); border: 1px solid var(--blue-200);
  border-radius: 10px; padding: 1rem 1.25rem; margin-top: 1rem;
}
.file-selected .fname { font-size: 14px; font-weight: 500; color: var(--blue-800); }
.file-selected .fsize { font-size: 12px; color: var(--gray-400); }
.file-remove { margin-left: auto; cursor: pointer; color: var(--gray-400); }
.file-remove:hover { color: var(--gray-900); }

/* Badge que mostra o tipo detectado */
.type-badge {
  font-size: 11px; font-weight: 500; padding: 2px 8px;
  border-radius: 5px; font-family: 'JetBrains Mono', monospace;
  flex-shrink: 0;
}
.type-dwg { background: var(--teal-50); color: var(--teal-600); border: 1px solid var(--teal-200); }
.type-dxf { background: var(--blue-50); color: var(--blue-600); border: 1px solid var(--blue-200); }

.options-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; }
.field label {
  display: block; font-size: 11px; font-weight: 500; color: var(--gray-400);
  margin-bottom: .4rem; text-transform: uppercase; letter-spacing: .05em;
}
select {
  width: 100%; appearance: none; background: var(--surface);
  border: 1px solid var(--gray-100); border-radius: var(--radius);
  padding: .55rem .9rem; font-size: 14px; color: var(--gray-900);
  cursor: pointer; outline: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24'%3E%3Cpath d='M6 9l6 6 6-6' stroke='%23888' fill='none' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat; background-position: right .75rem center; padding-right: 2rem;
  transition: border-color .2s;
}
select:focus { border-color: var(--blue-200); }

#btn-convert {
  width: 100%; padding: 1rem; border: none; border-radius: 12px;
  background: var(--blue-600); color: #fff; font-size: 15px; font-weight: 500;
  cursor: pointer; transition: background .2s, transform .1s;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  margin-top: 1rem;
}
#btn-convert:hover:not(:disabled) { background: var(--blue-800); }
#btn-convert:active:not(:disabled) { transform: scale(.99); }
#btn-convert:disabled { background: var(--gray-100); color: var(--gray-400); cursor: not-allowed; }
#btn-convert svg { width: 18px; height: 18px; stroke: currentColor; fill: none; stroke-width: 2; }

.progress-bar { height: 4px; background: var(--gray-100); border-radius: 99px; overflow: hidden; margin-top: 1rem; display: none; }
.progress-fill { height: 100%; width: 40%; background: var(--blue-600); border-radius: 99px; animation: slide 1.2s linear infinite; }
@keyframes slide { 0%{transform:translateX(-200%)} 100%{transform:translateX(400%)} }

.status-label { text-align: center; font-size: 13px; color: var(--gray-400); margin-top: .5rem; display: none; }

#error-box {
  display: none; background: var(--coral-50); border: 1px solid var(--coral-200);
  border-radius: 12px; padding: 1rem 1.25rem; margin-top: 1rem;
  color: var(--coral-600); font-size: 14px; line-height: 1.5;
}
#error-box strong { display: block; margin-bottom: .25rem; }

#result {
  display: none; margin-top: 1.25rem;
  background: var(--green-50); border: 1px solid var(--green-200);
  border-radius: 14px; padding: 1.5rem;
}
.result-header { display: flex; align-items: center; gap: 12px; margin-bottom: 1rem; }
.result-check {
  width: 38px; height: 38px; background: var(--green-600); border-radius: 50%;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.result-check svg { width: 20px; height: 20px; stroke: #fff; fill: none; stroke-width: 2.5; }
.result-title { font-weight: 600; font-size: 15px; color: var(--green-600); }
.result-sub   { font-size: 12px; color: var(--gray-400); }

.info-chips { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 1.25rem; }
.chip {
  font-size: 12px; font-weight: 500; padding: 4px 12px; background: #fff;
  border: 1px solid var(--gray-100); border-radius: 20px; color: var(--gray-700);
  font-family: 'JetBrains Mono', monospace;
}

#btn-download {
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--green-600); color: #fff; border: none; border-radius: 10px;
  padding: .7rem 1.5rem; font-size: 14px; font-weight: 500;
  cursor: pointer; text-decoration: none; transition: background .2s;
}
#btn-download:hover { background: var(--green-800); }
#btn-download svg { width: 16px; height: 16px; stroke: currentColor; fill: none; stroke-width: 2; }

footer { text-align: center; padding: 2rem; font-size: 12px; color: var(--gray-100); }
</style>
</head>
<body>

<header>
  <div class="logo">
    <div class="logo-icon">
      <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="16" y2="17"/></svg>
    </div>
    DWG/DXF → PDF
  </div>
  <span class="badge">Gratuito · sem cadastro</span>
</header>

<main>

  <div class="hero">
    <h1>Converta plantas CAD em PDF<br>com a escala certa</h1>
    <p>Faça upload do seu arquivo, escolha escala e papel — e receba o PDF pronto para imprimir.</p>
    <div class="formats">
      <span class="fmt-pill fmt-dwg">.DWG</span>
      <span class="fmt-arrow">→</span>
      <span class="fmt-pill fmt-dxf">.DXF</span>
      <span class="fmt-arrow">→</span>
      <span class="fmt-pill fmt-dxf">.PDF</span>
    </div>
  </div>

  <!-- Upload -->
  <div class="card">
    <div class="card-title">1 · Arquivo</div>

    <div id="dropzone">
      <input type="file" id="file-input" accept=".dxf,.dwg"/>
      <div class="drop-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
          <polyline points="17 8 12 3 7 8"/>
          <line x1="12" y1="3" x2="12" y2="15"/>
        </svg>
      </div>
      <h3>Arraste o arquivo aqui</h3>
      <p>ou clique para escolher · .DWG e .DXF aceitos</p>
    </div>

    <div id="file-info" style="display:none" class="file-selected">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#185FA5" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
      <div>
        <div class="fname" id="file-name">arquivo.dxf</div>
        <div class="fsize" id="file-size"></div>
      </div>
      <span id="type-badge" class="type-badge"></span>
      <span class="file-remove" onclick="clearFile()" title="Remover">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </span>
    </div>
  </div>

  <!-- Options -->
  <div class="card">
    <div class="card-title">2 · Configurações de impressão</div>
    <div class="options-grid">
      <div class="field">
        <label>Escala</label>
        <select id="sel-scale">
          <option value="auto" selected>Automático</option>
          <option value="1:1">1:1 (real)</option>
          <option value="1:2">1:2</option>
          <option value="1:5">1:5</option>
          <option value="1:10">1:10</option>
          <option value="1:20">1:20</option>
          <option value="1:25">1:25</option>
          <option value="1:50">1:50</option>
          <option value="1:100">1:100</option>
          <option value="1:200">1:200</option>
          <option value="1:500">1:500</option>
          <option value="1:1000">1:1000</option>
        </select>
      </div>
      <div class="field">
        <label>Papel</label>
        <select id="sel-paper">
          <option value="A4" selected>A4 (210×297)</option>
          <option value="A3">A3 (297×420)</option>
          <option value="A2">A2 (420×594)</option>
          <option value="A1">A1 (594×841)</option>
          <option value="A0">A0 (841×1189)</option>
          <option value="Letter">Letter (216×279)</option>
        </select>
      </div>
      <div class="field">
        <label>Orientação</label>
        <select id="sel-orient">
          <option value="auto" selected>Automático</option>
          <option value="portrait">Retrato</option>
          <option value="landscape">Paisagem</option>
        </select>
      </div>
    </div>
  </div>

  <button id="btn-convert" disabled onclick="convert()">
    <svg viewBox="0 0 24 24"><polyline points="16 16 12 12 8 16"/><line x1="12" y1="12" x2="12" y2="21"/><path d="M20.39 18.39A5 5 0 0 0 18 9h-1.26A8 8 0 1 0 3 16.3"/></svg>
    Converter para PDF
  </button>

  <div class="progress-bar" id="progress-wrap">
    <div class="progress-fill"></div>
  </div>
  <div class="status-label" id="status-label">Processando...</div>

  <div id="error-box">
    <strong>Não foi possível converter</strong>
    <span id="error-msg"></span>
  </div>

  <div id="result">
    <div class="result-header">
      <div class="result-check">
        <svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
      </div>
      <div>
        <div class="result-title">PDF gerado com sucesso!</div>
        <div class="result-sub">Pronto para download e impressão</div>
      </div>
    </div>
    <div class="info-chips" id="info-chips"></div>
    <a id="btn-download" href="#">
      <svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
      Baixar PDF
    </a>
  </div>

</main>

<footer>DWG/DXF → PDF Converter · Python + FastAPI + ezdxf + LibreDWG · Gratuito</footer>

<script>
let selectedFile = null;
const API = '';

const dropzone   = document.getElementById('dropzone');
const fileInput  = document.getElementById('file-input');
const fileInfo   = document.getElementById('file-info');
const btnConvert = document.getElementById('btn-convert');

dropzone.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', e => selectFile(e.target.files[0]));
dropzone.addEventListener('dragover', e => { e.preventDefault(); dropzone.classList.add('drag'); });
dropzone.addEventListener('dragleave', () => dropzone.classList.remove('drag'));
dropzone.addEventListener('drop', e => {
  e.preventDefault(); dropzone.classList.remove('drag');
  if (e.dataTransfer.files[0]) selectFile(e.dataTransfer.files[0]);
});

function selectFile(f) {
  selectedFile = f;
  const ext = f.name.split('.').pop().toLowerCase();
  document.getElementById('file-name').textContent = f.name;
  document.getElementById('file-size').textContent = (f.size / 1024).toFixed(1) + ' KB';

  const badge = document.getElementById('type-badge');
  badge.textContent = '.' + ext.toUpperCase();
  badge.className = 'type-badge ' + (ext === 'dwg' ? 'type-dwg' : 'type-dxf');

  fileInfo.style.display = 'flex';
  dropzone.style.display = 'none';
  btnConvert.disabled = false;

  // Reset previous result/error
  document.getElementById('result').style.display = 'none';
  document.getElementById('error-box').style.display = 'none';
}

function clearFile() {
  selectedFile = null;
  fileInput.value = '';
  fileInfo.style.display = 'none';
  dropzone.style.display = '';
  btnConvert.disabled = true;
}

const STEPS_DWG = ['Recebendo arquivo...', 'Convertendo DWG → DXF...', 'Renderizando geometria...', 'Gerando PDF...'];
const STEPS_DXF = ['Recebendo arquivo...', 'Renderizando geometria...', 'Gerando PDF...'];

async function convert() {
  if (!selectedFile) return;
  const isDwg = selectedFile.name.toLowerCase().endsWith('.dwg');
  const steps = isDwg ? STEPS_DWG : STEPS_DXF;

  setLoading(true, steps);

  const fd = new FormData();
  fd.append('file', selectedFile);
  fd.append('scale',       document.getElementById('sel-scale').value);
  fd.append('paper',       document.getElementById('sel-paper').value);
  fd.append('orientation', document.getElementById('sel-orient').value);

  try {
    const res  = await fetch(API + '/api/convert', { method: 'POST', body: fd });
    const data = await res.json();
    if (!res.ok) showError(data.detail || 'Erro desconhecido.');
    else         showResult(data);
  } catch(e) {
    showError('Não foi possível conectar ao servidor. Verifique sua conexão e tente novamente.');
  } finally {
    setLoading(false);
  }
}

let _stepTimer = null;
function setLoading(v, steps) {
  btnConvert.disabled = v;
  const icon = `<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 16 12 12 8 16"/><line x1="12" y1="12" x2="12" y2="21"/><path d="M20.39 18.39A5 5 0 0 0 18 9h-1.26A8 8 0 1 0 3 16.3"/></svg>`;
  btnConvert.innerHTML = v ? 'Convertendo…' : icon + ' Converter para PDF';

  document.getElementById('progress-wrap').style.display  = v ? '' : 'none';
  document.getElementById('status-label').style.display   = v ? '' : 'none';
  document.getElementById('error-box').style.display      = 'none';
  document.getElementById('result').style.display         = 'none';

  clearInterval(_stepTimer);
  if (v && steps) {
    let i = 0;
    const lbl = document.getElementById('status-label');
    lbl.textContent = steps[0];
    _stepTimer = setInterval(() => {
      i = Math.min(i + 1, steps.length - 1);
      lbl.textContent = steps[i];
    }, 1800);
  }
}

function showError(msg) {
  document.getElementById('error-msg').textContent = msg;
  document.getElementById('error-box').style.display = '';
}

function showResult(data) {
  const chips = document.getElementById('info-chips');
  chips.innerHTML = '';
  if (data.info) {
    Object.values(data.info).forEach(v => {
      const c = document.createElement('span');
      c.className = 'chip';
      c.textContent = v;
      chips.appendChild(c);
    });
  }
  document.getElementById('btn-download').href = API + data.download_url;
  document.getElementById('result').style.display = '';
}
</script>
</body>
</html>
