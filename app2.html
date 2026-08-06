<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Code Analyzer — Bugs, Math & Grammar</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{
    --bg: #f7f8fa;
    --surface: #ffffff;
    --border: #e4e7ec;
    --text: #1a1d21;
    --text-muted: #667085;
    --text-faint: #98a2b3;
    --primary: #4f46e5;
    --primary-dark: #4338ca;
    --primary-bg: #eef2ff;
    --red: #d92d20;
    --red-bg: #fef3f2;
    --amber: #b54708;
    --amber-bg: #fffaeb;
    --green: #067647;
    --green-bg: #ecfdf3;
    --teal: #0e7490;
    --teal-bg: #ecfeff;
    --radius: 10px;
    --shadow-sm: 0 1px 2px rgba(16,24,40,0.05);
    --shadow-md: 0 4px 12px rgba(16,24,40,0.08);
  }
 
  *{ box-sizing: border-box; }
  html,body{ margin:0; padding:0; }
 
  body{
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
  }
 
  a{ color: var(--primary); }
 
  ::-webkit-scrollbar{ width: 10px; height: 10px; }
  ::-webkit-scrollbar-track{ background: transparent; }
  ::-webkit-scrollbar-thumb{ background: #d0d5dd; border-radius: 6px; }
  ::-webkit-scrollbar-thumb:hover{ background: #98a2b3; }
 
  /* ============ TOP NAV ============ */
  nav.topbar{
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 0 1.75rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 20;
    flex-wrap: wrap;
    gap: 0.5rem;
  }
 
  .brand{
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-weight: 700;
    font-size: 1.05rem;
    padding: 0.9rem 0;
  }
 
  .brand .mark{
    width: 30px; height: 30px;
    border-radius: 8px;
    background: var(--primary);
    color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.95rem;
  }
 
  .page-tabs{
    display: flex;
    gap: 0.25rem;
  }
 
  .page-tab{
    font-family: 'Inter', sans-serif;
    font-size: 0.88rem;
    font-weight: 600;
    color: var(--text-muted);
    background: none;
    border: none;
    padding: 1rem 0.9rem;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    display: flex;
    align-items: center;
    gap: 0.45rem;
    transition: color 0.15s ease;
  }
 
  .page-tab:hover{ color: var(--text); }
 
  .page-tab.active{
    color: var(--primary);
    border-bottom-color: var(--primary);
  }
 
  .nav-right{
    display: flex;
    align-items: center;
    gap: 1.5rem;
    font-size: 0.85rem;
    color: var(--text-muted);
    padding: 0.9rem 0;
  }
 
  /* ============ LAYOUT ============ */
  .page{
    max-width: 1280px;
    margin: 0 auto;
    padding: 2rem 1.75rem 4rem;
  }
 
  .view{ display: none; }
  .view.active{ display: block; }
 
  .page-head{
    margin-bottom: 1.75rem;
  }
 
  .page-head h1{
    font-size: 1.6rem;
    font-weight: 800;
    margin: 0 0 0.35rem;
    letter-spacing: -0.02em;
  }
 
  .page-head p{
    color: var(--text-muted);
    margin: 0;
    font-size: 0.95rem;
  }
 
  .grid{
    display: grid;
    grid-template-columns: minmax(0,1fr) minmax(0,1fr);
    gap: 1.5rem;
    align-items: start;
  }
 
  @media (max-width: 900px){
    .grid{ grid-template-columns: 1fr; }
  }
 
  .panel{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow-sm);
    overflow: hidden;
  }
 
  .panel-head{
    padding: 1rem 1.25rem;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
  }
 
  .panel-head h2{
    font-size: 0.95rem;
    font-weight: 600;
    margin: 0;
  }
 
  .panel-body{ padding: 1.25rem; }
 
  /* language pills (also reused for math example pills) */
  .lang-pills{
    display: flex;
    gap: 0.4rem;
    background: var(--bg);
    padding: 0.25rem;
    border-radius: 8px;
    border: 1px solid var(--border);
    flex-wrap: wrap;
  }
 
  .lang-pill{
    font-family: 'Inter', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    padding: 0.4rem 0.75rem;
    border-radius: 6px;
    border: none;
    background: transparent;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.15s ease;
  }
 
  .lang-pill:hover{ color: var(--text); }
 
  .lang-pill.active{
    background: var(--surface);
    color: var(--text);
    box-shadow: var(--shadow-sm);
    font-weight: 600;
  }
 
  /* code / text editor shell */
  .editor-wrap{
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
  }
 
  .editor-topbar{
    background: #fafbfc;
    border-bottom: 1px solid var(--border);
    padding: 0.5rem 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }
 
  .dot{ width: 9px; height: 9px; border-radius: 50%; }
  .dot.r{ background: #ff5f57; }
  .dot.y{ background: #febc2e; }
  .dot.g{ background: #28c840; }
  .editor-filename{
    margin-left: 0.6rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-faint);
  }
 
  textarea.editor-input{
    width: 100%;
    min-height: 340px;
    border: none;
    background: #1a1d21;
    color: #e4e7ec;
    padding: 1rem 1.1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    line-height: 1.7;
    resize: vertical;
    outline: none;
    display: block;
  }
 
  textarea.editor-input::placeholder{ color: #667085; }
 
  textarea.prose-input{
    width: 100%;
    min-height: 340px;
    border: none;
    background: #ffffff;
    color: #1a1d21;
    padding: 1.1rem 1.2rem;
    font-family: 'Inter', sans-serif;
    font-size: 0.95rem;
    line-height: 1.75;
    resize: vertical;
    outline: none;
    display: block;
  }
  textarea.prose-input::placeholder{ color: var(--text-faint); }
 
  input.math-input{
    width: 100%;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.85rem 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.05rem;
    outline: none;
    background: #fafbfc;
  }
  input.math-input:focus{
    border-color: var(--primary);
    box-shadow: 0 0 0 3px var(--primary-bg);
  }
 
  .action-row{
    display: flex;
    gap: 0.7rem;
    margin-top: 1rem;
  }
 
  button.btn{
    font-family: 'Inter', sans-serif;
    font-size: 0.88rem;
    font-weight: 600;
    padding: 0.65rem 1.15rem;
    border-radius: 8px;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.15s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
  }
 
  button.btn.primary{
    background: var(--primary);
    color: #fff;
    flex: 1;
    justify-content: center;
  }
  button.btn.primary:hover{ background: var(--primary-dark); }
  button.btn.primary:disabled{ background: #c7c9f5; cursor: not-allowed; }
 
  button.btn.secondary{
    background: var(--surface);
    color: var(--text-muted);
    border-color: var(--border);
  }
  button.btn.secondary:hover{ background: var(--bg); color: var(--text); }
 
  /* ============ RESULTS (shared style) ============ */
  .empty-state{
    text-align: center;
    padding: 3.2rem 1.5rem;
    color: var(--text-faint);
  }
  .empty-state .icon{
    font-size: 1.8rem;
    margin-bottom: 0.7rem;
    display: block;
    opacity: 0.6;
  }
  .empty-state p{ margin: 0; font-size: 0.92rem; }
 
  .clean-state{
    text-align: center;
    padding: 2.6rem 1.5rem;
  }
  .clean-state .badge{
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--green-bg);
    color: var(--green);
    font-weight: 600;
    font-size: 0.9rem;
    padding: 0.5rem 1rem;
    border-radius: 20px;
  }
  .clean-state p{ margin-top: 1rem; color: var(--text-muted); font-size: 0.9rem; }
 
  .summary-row{
    display: flex;
    gap: 0.7rem;
    margin-bottom: 1.1rem;
    flex-wrap: wrap;
  }
 
  .summary-chip{
    flex: 1;
    min-width: 80px;
    text-align: center;
    padding: 0.8rem 0.5rem;
    border-radius: 8px;
    border: 1px solid var(--border);
  }
 
  .summary-chip .num{
    display: block;
    font-size: 1.5rem;
    font-weight: 800;
    line-height: 1;
  }
  .summary-chip .lbl{
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--text-muted);
    margin-top: 0.3rem;
    display: block;
  }
 
  .summary-chip.high{ background: var(--red-bg); }
  .summary-chip.high .num{ color: var(--red); }
  .summary-chip.medium{ background: var(--amber-bg); }
  .summary-chip.medium .num{ color: var(--amber); }
  .summary-chip.low{ background: var(--green-bg); }
  .summary-chip.low .num{ color: var(--green); }
  .summary-chip.info{ background: var(--teal-bg); }
  .summary-chip.info .num{ color: var(--teal); }
 
  .issue-list{
    display: flex;
    flex-direction: column;
    gap: 0.7rem;
    max-height: 560px;
    overflow-y: auto;
    padding-right: 0.25rem;
  }
 
  .issue{
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.95rem 1.05rem;
    border-left-width: 3px;
  }
 
  .issue.high{ border-left-color: var(--red); }
  .issue.medium{ border-left-color: var(--amber); }
  .issue.low{ border-left-color: var(--green); }
  .issue.info{ border-left-color: var(--teal); }
 
  .issue-head{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 0.7rem;
    margin-bottom: 0.35rem;
  }
 
  .issue-title{
    font-weight: 600;
    font-size: 0.92rem;
  }
 
  .badge-sev{
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    padding: 0.18rem 0.5rem;
    border-radius: 4px;
    white-space: nowrap;
    flex-shrink: 0;
  }
  .badge-sev.high{ background: var(--red-bg); color: var(--red); }
  .badge-sev.medium{ background: var(--amber-bg); color: var(--amber); }
  .badge-sev.low{ background: var(--green-bg); color: var(--green); }
  .badge-sev.info{ background: var(--teal-bg); color: var(--teal); }
 
  .issue-desc{
    font-size: 0.87rem;
    color: var(--text-muted);
    line-height: 1.55;
    margin-bottom: 0.6rem;
  }
 
  .issue-code{
    background: #1a1d21;
    color: #d5d8dd;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    padding: 0.55rem 0.75rem;
    border-radius: 6px;
    overflow-x: auto;
    white-space: pre-wrap;
    word-break: break-word;
  }
  .issue-code .lineno{ color: #667085; margin-right: 0.5rem; }
  .issue-code .code{ color: #f5c518; }
 
  .issue-fix{
    margin-top: 0.6rem;
    font-size: 0.83rem;
    color: var(--text);
    background: var(--primary-bg);
    border-radius: 6px;
    padding: 0.5rem 0.7rem;
  }
  .issue-fix b{ color: var(--primary-dark); }
 
  /* ============ LEARNING / STEP PANEL (shared) ============ */
  .learning-panel{ margin-top: 1.5rem; }
 
  .step-list{ display: flex; flex-direction: column; }
 
  .step-item{
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    padding: 0.85rem 0;
    border-bottom: 1px solid var(--border);
  }
  .step-item:last-child{ border-bottom: none; }
 
  .step-num{
    width: 26px; height: 26px;
    border-radius: 50%;
    background: var(--primary-bg);
    color: var(--primary-dark);
    font-size: 0.78rem;
    font-weight: 700;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }
 
  .step-text{ font-size: 0.9rem; padding-top: 0.15rem; }
 
  /* ============ MATH SOLVER SPECIFIC ============ */
  .math-result{
    text-align: center;
    padding: 1.5rem 1rem;
  }
  .math-result .answer{
    font-family: 'JetBrains Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-dark);
    margin-bottom: 0.4rem;
  }
  .math-result .expr{
    font-family: 'JetBrains Mono', monospace;
    color: var(--text-muted);
    font-size: 0.95rem;
  }
 
  .math-steps{
    margin-top: 1.3rem;
    text-align: left;
  }
 
  .math-step-row{
    display: flex;
    gap: 0.8rem;
    padding: 0.65rem 0;
    border-bottom: 1px dashed var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    align-items: baseline;
  }
  .math-step-row:last-child{ border-bottom: none; }
  .math-step-label{
    color: var(--text-muted);
    font-family: 'Inter', sans-serif;
    font-size: 0.78rem;
    min-width: 90px;
    flex-shrink: 0;
  }
 
  .example-list{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  .example-btn{
    text-align: left;
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.55rem 0.8rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: var(--text);
    cursor: pointer;
    transition: all 0.15s ease;
  }
  .example-btn:hover{ border-color: var(--primary); background: var(--primary-bg); }
 
  /* ============ GRAMMAR SPECIFIC ============ */
  .grammar-score-wrap{
    display: flex;
    align-items: center;
    gap: 1.2rem;
    margin-bottom: 1.1rem;
    padding: 1rem 1.1rem;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: var(--bg);
  }
  .grammar-score-ring{
    width: 56px; height: 56px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800;
    font-size: 1rem;
    flex-shrink: 0;
    color: #fff;
  }
  .grammar-score-meta{ font-size: 0.85rem; color: var(--text-muted); }
  .grammar-score-meta b{ color: var(--text); font-size: 1rem; display:block; margin-bottom:0.15rem; }
 
  .highlighted-text{
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem 1.1rem;
    font-size: 0.92rem;
    line-height: 1.85;
    background: #fafbfc;
    white-space: pre-wrap;
  }
  .flag{
    background: var(--amber-bg);
    border-bottom: 2px solid var(--amber);
    border-radius: 2px;
    padding: 0 1px;
  }
  .flag.high{ background: var(--red-bg); border-bottom-color: var(--red); }
 
  footer.site-footer{
    text-align: center;
    padding: 2rem 1rem 3rem;
    font-size: 0.8rem;
    color: var(--text-faint);
  }
 
  @media (prefers-reduced-motion: reduce){
    *{ transition: none !important; }
  }
</style>
</head>
<body>
 
<nav class="topbar">
  <div class="brand">
    <span class="mark">◆</span>
    Analyzer Suite
  </div>
  <div class="page-tabs" id="pageTabs">
    <button class="page-tab active" data-page="bugs">🐞 Bug Scanner</button>
    <button class="page-tab" data-page="math">Σ Math Solver</button>
    <button class="page-tab" data-page="grammar">✎ Grammar Checker</button>
  </div>
  <div class="nav-right">
    <span id="statusLine">Ready</span>
  </div>
</nav>
 
<div class="page">
 
  <!-- ============ PAGE 1: BUG SCANNER ============ -->
  <div class="view active" id="view-bugs">
    <div class="page-head">
      <h1>Find bugs. Learn the pattern.</h1>
      <p>Paste your code, run a scan, and get a personalized set of things to study based on what came up.</p>
    </div>
 
    <div class="grid">
      <section class="panel">
        <div class="panel-head">
          <h2>Your code</h2>
          <div class="lang-pills" id="langRow">
            <button class="lang-pill active" data-lang="python">Python</button>
            <button class="lang-pill" data-lang="javascript">JavaScript</button>
            <button class="lang-pill" data-lang="java">Java</button>
            <button class="lang-pill" data-lang="cpp">C++</button>
          </div>
        </div>
        <div class="panel-body">
          <div class="editor-wrap">
            <div class="editor-topbar">
              <span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
              <span class="editor-filename" id="filenameLabel">main.py</span>
            </div>
            <textarea class="editor-input" id="codeInput" spellcheck="false" placeholder="Paste your code here…"></textarea>
          </div>
          <div class="action-row">
            <button class="btn primary" id="analyzeBtn">Scan code</button>
            <button class="btn secondary" id="clearBtn">Clear</button>
          </div>
        </div>
      </section>
 
      <section class="panel">
        <div class="panel-head">
          <h2>Results</h2>
          <span id="resultCountLabel" style="font-size:0.8rem; color:var(--text-muted);"></span>
        </div>
        <div class="panel-body">
          <div id="resultsPanel">
            <div class="empty-state">
              <span class="icon">↗</span>
              <p>Run a scan to see results here.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
 
    <section class="panel learning-panel" id="learningPanel" style="display:none;">
      <div class="panel-head"><h2>Suggested learning path</h2></div>
      <div class="panel-body"><div class="step-list" id="stepList"></div></div>
    </section>
  </div>
 
  <!-- ============ PAGE 2: MATH SOLVER ============ -->
  <div class="view" id="view-math">
    <div class="page-head">
      <h1>Solve arithmetic & algebra.</h1>
      <p>Type an expression to calculate, or an equation with "=" to solve for x — see the steps behind the answer.</p>
    </div>
 
    <div class="grid">
      <section class="panel">
        <div class="panel-head"><h2>Enter a problem</h2></div>
        <div class="panel-body">
          <input class="math-input" id="mathInput" placeholder="e.g. 3x + 5 = 20   or   (4 + 6) * 2 - 3^2" autocomplete="off">
          <div class="action-row">
            <button class="btn primary" id="solveBtn">Solve</button>
            <button class="btn secondary" id="mathClearBtn">Clear</button>
          </div>
 
          <div style="margin-top:1.4rem;">
            <div style="font-size:0.8rem; font-weight:600; color:var(--text-muted); margin-bottom:0.6rem; text-transform:uppercase; letter-spacing:0.04em;">Try an example</div>
            <div class="example-list" id="mathExamples">
              <button class="example-btn" data-eq="3x + 5 = 20">3x + 5 = 20</button>
              <button class="example-btn" data-eq="2x^2 - 8x + 6 = 0">2x^2 - 8x + 6 = 0</button>
              <button class="example-btn" data-eq="(4 + 6) * 2 - 3^2">(4 + 6) * 2 - 3^2</button>
              <button class="example-btn" data-eq="x/2 + 7 = 10">x/2 + 7 = 10</button>
              <button class="example-btn" data-eq="sqrt(144) + 5*3">sqrt(144) + 5*3</button>
            </div>
          </div>
        </div>
      </section>
 
      <section class="panel">
        <div class="panel-head"><h2>Solution</h2></div>
        <div class="panel-body">
          <div id="mathResultsPanel">
            <div class="empty-state">
              <span class="icon">Σ</span>
              <p>Enter a problem and press Solve.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
 
  <!-- ============ PAGE 3: GRAMMAR CHECKER ============ -->
  <div class="view" id="view-grammar">
    <div class="page-head">
      <h1>Check sentences & grammar.</h1>
      <p>Paste text to catch punctuation slips, mixed-up words, run-ons, and other common writing issues.</p>
    </div>
 
    <div class="grid">
      <section class="panel">
        <div class="panel-head"><h2>Your text</h2></div>
        <div class="panel-body">
          <div class="editor-wrap">
            <textarea class="prose-input" id="textInput" spellcheck="false" placeholder="Paste a sentence or paragraph here…"></textarea>
          </div>
          <div class="action-row">
            <button class="btn primary" id="checkBtn">Check writing</button>
            <button class="btn secondary" id="textClearBtn">Clear</button>
          </div>
        </div>
      </section>
 
      <section class="panel">
        <div class="panel-head">
          <h2>Feedback</h2>
          <span id="grammarCountLabel" style="font-size:0.8rem; color:var(--text-muted);"></span>
        </div>
        <div class="panel-body">
          <div id="grammarResultsPanel">
            <div class="empty-state">
              <span class="icon">✎</span>
              <p>Run a check to see feedback here.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
 
    <section class="panel learning-panel" id="grammarPreviewPanel" style="display:none;">
      <div class="panel-head"><h2>Your text, with issues marked</h2></div>
      <div class="panel-body"><div class="highlighted-text" id="highlightedText"></div></div>
    </section>
  </div>
 
</div>
 
<footer class="site-footer">Runs entirely in your browser — nothing you type is sent anywhere.</footer>
 
<script>
(function(){
  // =================================================================
  // NAVIGATION
  // =================================================================
  const pageTabs = document.getElementById('pageTabs');
  const views = { bugs: document.getElementById('view-bugs'), math: document.getElementById('view-math'), grammar: document.getElementById('view-grammar') };
  pageTabs.addEventListener('click', e => {
    const btn = e.target.closest('.page-tab');
    if (!btn) return;
    [...pageTabs.children].forEach(b => b.classList.toggle('active', b === btn));
    Object.entries(views).forEach(([key, el]) => el.classList.toggle('active', key === btn.dataset.page));
  });
 
  function escapeHtml(str){
    return str.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }
 
  const statusLine = document.getElementById('statusLine');
 
  // =================================================================
  // PAGE 1 — BUG SCANNER  (unchanged logic from before)
  // =================================================================
  const BUG_PATTERNS = {
    javascript: [
      { re: /for\s*\([^;]*;\s*[^<>=!]*<=\s*[^.]*\.length/g, severity:'high', title:'Array index out of bounds',
        desc:'Using <= with array.length will access an undefined element past the final index.',
        fix:'Change <= to < in the loop condition.',
        concept:'Array Indexing', learning:'Arrays are zero-indexed. Use < instead of <= in the loop condition.' },
      { re: /==\s*null|null\s*==/g, severity:'medium', title:'Loose equality with null',
        desc:'Using == can trigger type coercion and match null against undefined unexpectedly.',
        fix:'Use === for a strict, predictable comparison.',
        concept:'Type Coercion', learning:'Always use === for strict, predictable comparisons.' },
      { re: /\bvar\s+\w+/g, severity:'low', title:'Using var instead of let/const',
        desc:'var has function scope and is hoisted, which can cause confusing bugs.',
        fix:'Replace var with let or const.',
        concept:'Variable Declarations', learning:'Use let or const to get proper block scoping.' },
    ],
    python: [
      { re: /except\s*:/g, severity:'high', title:'Bare except clause',
        desc:'Catches every exception, including ones you never intended to hide, masking real bugs.',
        fix:'Catch a specific exception type, e.g. except ValueError:',
        concept:'Exception Handling', learning:'Specify the exception types you actually expect to handle.' },
      { re: /==\s*True|True\s*==|==\s*False|False\s*==/g, severity:'medium', title:'Explicit True/False comparison',
        desc:'Comparing directly to True or False is redundant and less idiomatic.',
        fix:'Use "if value:" instead of "if value == True:".',
        concept:'Boolean Logic', learning:'Rely on truthiness — use "if value:" instead of "if value == True:".' },
      { re: /print\s*\(/g, severity:'low', title:'Debug print statements',
        desc:'Leftover print statements clutter output and don\u2019t respect log levels.',
        fix:'Swap print() for logging.debug() or similar.',
        concept:'Debugging', learning:'Swap print() for a proper logging framework with levels.' },
      { re: /range\(len\([^)]+\)\)/g, severity:'medium', title:'Using range(len()) pattern',
        desc:'Indexing manually through range(len(x)) is less readable than iterating directly.',
        fix:'Use enumerate(items) instead.',
        concept:'Pythonic Code', learning:'Use enumerate() to get index and value together.' },
    ],
    java: [
      { re: /==\s*"[^"]*"|"[^"]*"\s*==/g, severity:'high', title:'String comparison with ==',
        desc:'== compares object references in Java, not string contents — this often works "by accident" then fails.',
        fix:'Use .equals() to compare string content.',
        concept:'String Comparison', learning:'Use .equals() (or .equalsIgnoreCase()) to compare string content.' },
      { re: /catch\s*\([^)]*\)\s*\{\s*\}/g, severity:'medium', title:'Empty catch block',
        desc:'Swallowing an exception silently hides failures that should surface somewhere.',
        fix:'Log the exception or handle it meaningfully.',
        concept:'Exception Handling', learning:'Log the exception or handle it meaningfully — never leave catch empty.' },
    ],
    cpp: [
      { re: /delete\s+\w+\s*;/g, severity:'high', title:'Using delete instead of delete[]',
        desc:'Freeing an array with plain delete instead of delete[] causes undefined behavior.',
        fix:'Use delete[] to free arrays allocated with new[].',
        concept:'Memory Management', learning:'Match new[] with delete[], and plain new with plain delete.' },
    ],
  };
 
  const BUG_LEARNING_PATHS = {
    'Array Indexing': ['Understand zero-based indexing', 'Practice writing loop boundaries by hand', 'Learn built-in array iteration methods'],
    'Type Coercion': ['Learn the difference between == and ===', 'Study JavaScript type conversion rules', 'Practice comparing mixed types safely'],
    'Exception Handling': ['Learn the exception hierarchy for your language', 'Study how errors should propagate', 'Practice structured logging instead of silent catches'],
    'Boolean Logic': ['Understand truthy vs. falsy values', 'Learn short-circuit operators', 'Study clean conditional style'],
    'String Comparison': ['Learn how references differ from values', 'Study .equals() and content comparison', 'Practice safe null-aware comparisons'],
    'Pythonic Code': ['Learn core Python idioms', 'Study list/dict comprehensions', 'Practice rewriting loops the idiomatic way'],
    'Debugging': ['Learn the logging module basics', 'Study log levels (debug/info/warn/error)', 'Practice attaching context to log messages'],
    'Memory Management': ['Learn stack vs. heap allocation', 'Study RAII and smart pointers', 'Practice pairing every allocation with its correct release'],
  };
 
  const BUG_EXAMPLES = {
    python: 'def calculate_total(items):\n    for i in range(len(items)):\n        pass\ntry:\n    result = calculate()\nexcept:\n    print("Error")\nif done == True:\n    print("finished")',
    javascript: 'for (let i = 0; i <= arr.length; i++) {\n    console.log(arr[i]);\n}\nvar x = 10;\nif (x == null) {\n    console.log("empty");\n}',
    java: 'String name1 = "John";\nif (name1 == "John") {\n    System.out.println("match");\n}\ntry {\n    risky();\n} catch (Exception e) {}',
    cpp: 'int* arr = new int[10];\ndelete arr;\n',
  };
 
  const FILENAMES = { python:'main.py', javascript:'main.js', java:'Main.java', cpp:'main.cpp' };
 
  let currentLang = 'python';
  const codeInput = document.getElementById('codeInput');
  const langRow = document.getElementById('langRow');
  const resultsPanel = document.getElementById('resultsPanel');
  const learningPanel = document.getElementById('learningPanel');
  const stepList = document.getElementById('stepList');
  const resultCountLabel = document.getElementById('resultCountLabel');
  const filenameLabel = document.getElementById('filenameLabel');
  const analyzeBtn = document.getElementById('analyzeBtn');
 
  function setLanguage(lang){
    currentLang = lang;
    [...langRow.children].forEach(b => b.classList.toggle('active', b.dataset.lang === lang));
    codeInput.value = BUG_EXAMPLES[lang] || '';
    filenameLabel.textContent = FILENAMES[lang] || 'main';
  }
 
  function detectBugs(code, lang){
    const patterns = BUG_PATTERNS[lang] || [];
    const bugs = [];
    for (const p of patterns){
      const re = new RegExp(p.re.source, p.re.flags);
      let m;
      while ((m = re.exec(code)) !== null){
        const lineNumber = code.slice(0, m.index).split('\n').length;
        bugs.push({ severity: p.severity, title: p.title, description: p.desc, fix: p.fix, concept: p.concept, match: m[0].trim(), line: lineNumber });
        if (m[0].length === 0) re.lastIndex++;
      }
    }
    bugs.sort((a,b) => a.line - b.line);
    return bugs;
  }
 
  function buildBugLearningPath(bugs){
    const concepts = [...new Set(bugs.map(b => b.concept))];
    const steps = [];
    for (const c of concepts){
      const s = BUG_LEARNING_PATHS[c] || ['Study the fundamentals of ' + c];
      for (const step of s) if (!steps.includes(step)) steps.push(step);
    }
    return steps.slice(0, 8);
  }
 
  function renderBugsEmpty(){
    resultsPanel.innerHTML = `<div class="empty-state"><span class="icon">↗</span><p>Run a scan to see results here.</p></div>`;
    learningPanel.style.display = 'none';
    resultCountLabel.textContent = '';
  }
 
  function renderBugResults(bugs){
    if (bugs.length === 0){
      resultsPanel.innerHTML = `<div class="clean-state"><div class="badge">✓ No issues found</div><p>Nothing matched our known bug patterns. Nice work.</p></div>`;
      learningPanel.style.display = 'none';
      resultCountLabel.textContent = '0 issues';
      return;
    }
    const high = bugs.filter(b => b.severity === 'high').length;
    const med = bugs.filter(b => b.severity === 'medium').length;
    const low = bugs.filter(b => b.severity === 'low').length;
    resultCountLabel.textContent = `${bugs.length} issue${bugs.length === 1 ? '' : 's'}`;
 
    let html = `<div class="summary-row">
        <div class="summary-chip high"><span class="num">${high}</span><span class="lbl">High</span></div>
        <div class="summary-chip medium"><span class="num">${med}</span><span class="lbl">Medium</span></div>
        <div class="summary-chip low"><span class="num">${low}</span><span class="lbl">Low</span></div>
      </div><div class="issue-list">`;
    for (const bug of bugs){
      html += `<div class="issue ${bug.severity}">
          <div class="issue-head"><div class="issue-title">${escapeHtml(bug.title)}</div><div class="badge-sev ${bug.severity}">${bug.severity}</div></div>
          <div class="issue-desc">${escapeHtml(bug.description)}</div>
          <div class="issue-code"><span class="lineno">Line ${bug.line}</span><span class="code">${escapeHtml(bug.match.slice(0,72))}</span></div>
          <div class="issue-fix"><b>Fix:</b> ${escapeHtml(bug.fix)}</div>
        </div>`;
    }
    html += `</div>`;
    resultsPanel.innerHTML = html;
 
    const path = buildBugLearningPath(bugs);
    stepList.innerHTML = path.map((step, i) => `<div class="step-item"><div class="step-num">${i+1}</div><div class="step-text">${escapeHtml(step)}</div></div>`).join('');
    learningPanel.style.display = '';
  }
 
  function analyzeCode(){
    const code = codeInput.value;
    if (!code.trim()){ renderBugsEmpty(); return; }
    statusLine.textContent = 'Scanning…';
    analyzeBtn.disabled = true;
    resultsPanel.innerHTML = `<div class="empty-state"><span class="icon">•••</span><p>Scanning your code…</p></div>`;
    setTimeout(() => {
      renderBugResults(detectBugs(code, currentLang));
      analyzeBtn.disabled = false;
      statusLine.textContent = 'Ready';
    }, 300);
  }
 
  langRow.addEventListener('click', e => {
    const btn = e.target.closest('.lang-pill');
    if (!btn) return;
    setLanguage(btn.dataset.lang);
    renderBugsEmpty();
  });
  analyzeBtn.addEventListener('click', analyzeCode);
  document.getElementById('clearBtn').addEventListener('click', () => { codeInput.value = ''; renderBugsEmpty(); });
  setLanguage('python');
 
  // =================================================================
  // PAGE 2 — MATH SOLVER
  // =================================================================
  const mathInput = document.getElementById('mathInput');
  const mathResultsPanel = document.getElementById('mathResultsPanel');
  const solveBtn = document.getElementById('solveBtn');
 
  // ---- Safe arithmetic expression parser (recursive descent) ----
  function evaluateExpression(exprStr){
    let i = 0;
    const s = exprStr.replace(/\s+/g, '');
 
    function peek(){ return s[i]; }
    function error(msg){ throw new Error(msg); }
 
    function parseExpr(){
      let val = parseTerm();
      while (peek() === '+' || peek() === '-'){
        const op = s[i++];
        const rhs = parseTerm();
        val = op === '+' ? val + rhs : val - rhs;
      }
      return val;
    }
    function parseTerm(){
      let val = parseFactor();
      while (peek() === '*' || peek() === '/'){
        const op = s[i++];
        const rhs = parseFactor();
        if (op === '/'){
          if (rhs === 0) error('Division by zero');
          val = val / rhs;
        } else val = val * rhs;
      }
      return val;
    }
    function parseFactor(){
      // handle unary minus/plus
      if (peek() === '-'){ i++; return -parseFactor(); }
      if (peek() === '+'){ i++; return parseFactor(); }
      let val = parseBase();
      if (peek() === '^'){ i++; const exp = parseFactor(); val = Math.pow(val, exp); }
      return val;
    }
    function parseBase(){
      if (peek() === '('){
        i++;
        const val = parseExpr();
        if (peek() !== ')') error('Missing closing parenthesis');
        i++;
        return val;
      }
      // function call e.g. sqrt(...)
      const funcMatch = /^(sqrt|abs|sin|cos|tan|log)/.exec(s.slice(i));
      if (funcMatch){
        const fname = funcMatch[1];
        i += fname.length;
        if (peek() !== '(') error('Expected ( after ' + fname);
        i++;
        const arg = parseExpr();
        if (peek() !== ')') error('Missing closing parenthesis');
        i++;
        const fns = { sqrt: Math.sqrt, abs: Math.abs, sin: Math.sin, cos: Math.cos, tan: Math.tan, log: Math.log10 };
        return fns[fname](arg);
      }
      const numMatch = /^\d+(\.\d+)?/.exec(s.slice(i));
      if (numMatch){
        i += numMatch[0].length;
        return parseFloat(numMatch[0]);
      }
      error('Unexpected character: ' + (peek() || 'end of input'));
    }
 
    const result = parseExpr();
    if (i < s.length) error('Unexpected trailing input: ' + s.slice(i));
    return result;
  }
 
  // ---- Equation side parser: returns {0: const, 1: coeff_x, 2: coeff_x2} ----
  function parsePolynomialSide(sideStr){
    let s = sideStr.replace(/\s+/g, '');
    if (s === '') error_poly();
    if (s[0] !== '+' && s[0] !== '-') s = '+' + s;
    const terms = s.match(/[+-][^+-]+/g);
    if (!terms) return null;
    const coeffs = {0:0, 1:0, 2:0};
    for (const term of terms){
      const sign = term[0] === '-' ? -1 : 1;
      const rest = term.slice(1);
      const m = /^(\d*\.?\d*)(x(\^(\d+))?)?(\/(\d+\.?\d*))?$/i.exec(rest);
      if (!m || rest === '') return null;
      const coeffStr = m[1];
      const hasX = !!m[2];
      const power = hasX ? (m[4] ? parseInt(m[4],10) : 1) : 0;
      if (power > 2) return null; // unsupported degree
      let coeff = coeffStr === '' ? (hasX ? 1 : (rest === '' ? 0 : NaN)) : parseFloat(coeffStr);
      if (isNaN(coeff)) return null;
      if (m[6]) coeff = coeff / parseFloat(m[6]);
      coeff *= sign;
      coeffs[power] = (coeffs[power] || 0) + coeff;
    }
    return coeffs;
  }
  function error_poly(){ throw new Error('empty side'); }
 
  function solveEquation(eqStr){
    const parts = eqStr.split('=');
    if (parts.length !== 2) throw new Error('An equation needs exactly one "=" sign.');
    const left = parsePolynomialSide(parts[0]);
    const right = parsePolynomialSide(parts[1]);
    if (!left || !right) throw new Error('Could not parse that equation. Supported terms: numbers, x, x^2, +, -, / by a number.');
 
    const a = (left[2]||0) - (right[2]||0);
    const b = (left[1]||0) - (right[1]||0);
    const c = (left[0]||0) - (right[0]||0);
 
    const steps = [];
    steps.push({ label: 'Standard form', value: `${fmtCoeff(a,'x^2')}${fmtCoeff(b,'x',true)}${fmtConst(c,true)} = 0` });
 
    if (Math.abs(a) < 1e-12){
      // linear
      if (Math.abs(b) < 1e-12){
        if (Math.abs(c) < 1e-12) return { steps, answer: 'Infinitely many solutions', detail: 'Every value of x satisfies this equation.' };
        return { steps, answer: 'No solution', detail: 'This equation reduces to a false statement (e.g. 0 = 5).' };
      }
      const x = -c / b;
      steps.push({ label: 'Isolate x', value: `x = ${fmtNum(-c)} / ${fmtNum(b)}` });
      return { steps, answer: `x = ${fmtNum(x)}`, detail: 'Linear equation — one solution.' };
    }
 
    // quadratic
    const disc = b*b - 4*a*c;
    steps.push({ label: 'Discriminant', value: `b² − 4ac = ${fmtNum(b)}² − 4(${fmtNum(a)})(${fmtNum(c)}) = ${fmtNum(disc)}` });
    if (disc < 0){
      const re = (-b/(2*a));
      const im = Math.sqrt(-disc)/(2*a);
      return { steps, answer: `x = ${fmtNum(re)} ± ${fmtNum(Math.abs(im))}i`, detail: 'Negative discriminant — two complex solutions.' };
    }
    const sq = Math.sqrt(disc);
    const x1 = (-b + sq) / (2*a);
    const x2 = (-b - sq) / (2*a);
    steps.push({ label: 'Quadratic formula', value: `x = (−b ± √disc) / (2a)` });
    if (Math.abs(x1 - x2) < 1e-9){
      return { steps, answer: `x = ${fmtNum(x1)}`, detail: 'One repeated real solution (discriminant = 0).' };
    }
    return { steps, answer: `x = ${fmtNum(x1)}  or  x = ${fmtNum(x2)}`, detail: 'Two real solutions.' };
  }
 
  function fmtNum(n){
    const r = Math.round(n * 1e6) / 1e6;
    return Number.isInteger(r) ? String(r) : String(r);
  }
  function fmtCoeff(v, sym, withSign){
    if (Math.abs(v) < 1e-12) return '';
    const sign = v < 0 ? '- ' : (withSign ? '+ ' : '');
    const abs = Math.abs(v);
    const coeffPart = abs === 1 ? '' : fmtNum(abs);
    return ` ${sign}${coeffPart}${sym}`;
  }
  function fmtConst(v, withSign){
    if (Math.abs(v) < 1e-12) return '';
    const sign = v < 0 ? '- ' : (withSign ? '+ ' : '');
    return ` ${sign}${fmtNum(Math.abs(v))}`;
  }
 
  function looksLikeEquation(str){ return str.includes('='); }
 
  function renderMathEmpty(){
    mathResultsPanel.innerHTML = `<div class="empty-state"><span class="icon">Σ</span><p>Enter a problem and press Solve.</p></div>`;
  }
 
  function renderMathError(msg){
    mathResultsPanel.innerHTML = `<div class="issue high"><div class="issue-head"><div class="issue-title">Couldn't solve that</div><div class="badge-sev high">error</div></div><div class="issue-desc">${escapeHtml(msg)}</div></div>`;
  }
 
  function renderMathArithmetic(exprStr, value){
    mathResultsPanel.innerHTML = `
      <div class="math-result">
        <div class="expr">${escapeHtml(exprStr)}</div>
        <div class="answer">= ${escapeHtml(fmtNum(value))}</div>
      </div>`;
  }
 
  function renderMathEquation(eqStr, result){
    let stepsHtml = result.steps.map(s => `
      <div class="math-step-row"><span class="math-step-label">${escapeHtml(s.label)}</span><span>${escapeHtml(s.value)}</span></div>
    `).join('');
    mathResultsPanel.innerHTML = `
      <div class="math-result">
        <div class="expr">${escapeHtml(eqStr)}</div>
        <div class="answer">${escapeHtml(result.answer)}</div>
        <div style="color:var(--text-muted); font-size:0.85rem;">${escapeHtml(result.detail)}</div>
        <div class="math-steps">${stepsHtml}</div>
      </div>`;
  }
 
  function solveMath(){
    const raw = mathInput.value.trim();
    if (!raw){ renderMathEmpty(); return; }
    try{
      if (looksLikeEquation(raw)){
        const result = solveEquation(raw);
        renderMathEquation(raw, result);
      } else {
        const value = evaluateExpression(raw);
        renderMathArithmetic(raw, value);
      }
    } catch(err){
      renderMathError(err.message || 'Please check your syntax and try again.');
    }
  }
 
  solveBtn.addEventListener('click', solveMath);
  mathInput.addEventListener('keydown', e => { if (e.key === 'Enter') solveMath(); });
  document.getElementById('mathClearBtn').addEventListener('click', () => { mathInput.value=''; renderMathEmpty(); });
  document.getElementById('mathExamples').addEventListener('click', e => {
    const btn = e.target.closest('.example-btn');
    if (!btn) return;
    mathInput.value = btn.dataset.eq;
    solveMath();
  });
 
  // =================================================================
  // PAGE 3 — GRAMMAR CHECKER
  // =================================================================
  const textInput = document.getElementById('textInput');
  const grammarResultsPanel = document.getElementById('grammarResultsPanel');
  const grammarCountLabel = document.getElementById('grammarCountLabel');
  const grammarPreviewPanel = document.getElementById('grammarPreviewPanel');
  const highlightedText = document.getElementById('highlightedText');
  const checkBtn = document.getElementById('checkBtn');
 
  const CONFUSABLE_WORDS = {
    'there': 'Commonly confused with "their" (possession) or "they\'re" (they are). Double-check usage.',
    'their': 'Commonly confused with "there" (location) or "they\'re" (they are). Double-check usage.',
    "they're": 'Commonly confused with "there" or "their". Double-check usage.',
    'your': 'Commonly confused with "you\'re" (you are). Double-check usage.',
    "you're": 'Commonly confused with "your" (possession). Double-check usage.',
    'its': 'Commonly confused with "it\'s" (it is). Double-check usage.',
    "it's": 'Commonly confused with "its" (possession). Double-check usage.',
    'then': 'Commonly confused with "than" (comparison). Double-check usage.',
    'than': 'Commonly confused with "then" (time/sequence). Double-check usage.',
    'affect': 'Commonly confused with "effect" (usually a noun). Double-check usage.',
    'effect': 'Commonly confused with "affect" (usually a verb). Double-check usage.',
    'loose': 'Commonly confused with "lose". Double-check usage.',
    'lose': 'Commonly confused with "loose". Double-check usage.',
    'to': 'Commonly confused with "too" (also/excessively) or "two" (2). Double-check usage.',
    'too': 'Commonly confused with "to". Double-check usage.',
  };
 
  function splitSentences(text){
    const matches = text.match(/[^.!?]+[.!?]*/g) || [];
    return matches.map(m => m.trim()).filter(Boolean);
  }
 
  function analyzeText(text){
    const issues = [];
    const highlights = []; // {start, end, severity}
 
    // 1. Double spaces
    let m;
    const dbl = /[ ]{2,}/g;
    while ((m = dbl.exec(text)) !== null){
      issues.push({ severity:'low', title:'Double space', description:'Extra whitespace between words.', snippet: text.slice(Math.max(0,m.index-15), m.index+15).trim() });
      highlights.push({ start:m.index, end:m.index+m[0].length, severity:'low' });
    }
 
    // 2. Repeated consecutive words
    const rep = /\b(\w+)\s+\1\b/gi;
    while ((m = rep.exec(text)) !== null){
      issues.push({ severity:'medium', title:'Repeated word', description:`"${m[1]}" appears twice in a row.`, snippet: m[0] });
      highlights.push({ start:m.index, end:m.index+m[0].length, severity:'medium' });
    }
 
    // 3. Lowercase standalone "i"
    const loneI = /\bi\b/g;
    while ((m = loneI.exec(text)) !== null){
      issues.push({ severity:'medium', title:'Lowercase "i"', description:'The pronoun "I" should always be capitalized.', snippet: text.slice(Math.max(0,m.index-10), m.index+11).trim() });
      highlights.push({ start:m.index, end:m.index+1, severity:'medium' });
    }
 
    // 4. Excess punctuation (!!! or ???)
    const excess = /[!?]{2,}/g;
    while ((m = excess.exec(text)) !== null){
      issues.push({ severity:'low', title:'Excessive punctuation', description:'Multiple exclamation/question marks read as informal.', snippet: m[0] });
      highlights.push({ start:m.index, end:m.index+m[0].length, severity:'low' });
    }
 
    // 5. Confusable words
    const wordRe = /\b[a-zA-Z']+\b/g;
    while ((m = wordRe.exec(text)) !== null){
      const w = m[0].toLowerCase();
      if (CONFUSABLE_WORDS[w]){
        issues.push({ severity:'low', title:`Check word choice: "${m[0]}"`, description: CONFUSABLE_WORDS[w], snippet: text.slice(Math.max(0,m.index-20), m.index+20).trim() });
        highlights.push({ start:m.index, end:m.index+m[0].length, severity:'low' });
      }
    }
 
    // Sentence-level checks
    const sentences = splitSentences(text);
    let cursor = 0;
    for (const sent of sentences){
      const idx = text.indexOf(sent, cursor);
      cursor = idx + sent.length;
      const trimmed = sent.trim();
      if (!trimmed) continue;
 
      // 6. Missing capitalization at sentence start
      const firstChar = trimmed[0];
      if (/[a-z]/.test(firstChar)){
        issues.push({ severity:'medium', title:'Sentence should start with a capital letter', description:'The first word of a sentence should be capitalized.', snippet: trimmed.slice(0,40) });
        highlights.push({ start: idx, end: idx+1, severity:'medium' });
      }
 
      // 7. Missing end punctuation
      if (!/[.!?]["')\]]?$/.test(trimmed)){
        issues.push({ severity:'medium', title:'Missing end punctuation', description:'This sentence doesn\u2019t end with a period, question mark, or exclamation point.', snippet: trimmed.slice(-40) });
      }
 
      // 8. Long sentence
      const wordCount = trimmed.split(/\s+/).filter(Boolean).length;
      if (wordCount > 30){
        issues.push({ severity:'low', title:'Long sentence', description:`This sentence runs ${wordCount} words — consider splitting it for clarity.`, snippet: trimmed.slice(0,50) + '…' });
      }
 
      // 9. Basic passive voice heuristic
      const passive = /\b(is|are|was|were|be|been|being)\s+\w+ed\b/i.exec(trimmed);
      if (passive){
        issues.push({ severity:'low', title:'Possible passive voice', description:'Consider rewriting in active voice for a more direct tone.', snippet: passive[0] });
      }
    }
 
    return { issues, highlights, wordCount: (text.match(/\b\w+\b/g) || []).length, sentenceCount: sentences.length };
  }
 
  function buildHighlightedHtml(text, highlights){
    if (highlights.length === 0) return escapeHtml(text);
    highlights.sort((a,b) => a.start - b.start);
    // merge overlaps, keep highest severity
    const merged = [];
    for (const h of highlights){
      const last = merged[merged.length-1];
      if (last && h.start <= last.end){
        last.end = Math.max(last.end, h.end);
        if (h.severity === 'high') last.severity = 'high';
      } else merged.push({...h});
    }
    let html = '';
    let pos = 0;
    for (const h of merged){
      html += escapeHtml(text.slice(pos, h.start));
      html += `<span class="flag ${h.severity === 'medium' ? 'high' : ''}">${escapeHtml(text.slice(h.start, h.end))}</span>`;
      pos = h.end;
    }
    html += escapeHtml(text.slice(pos));
    return html;
  }
 
  function renderGrammarEmpty(){
    grammarResultsPanel.innerHTML = `<div class="empty-state"><span class="icon">✎</span><p>Run a check to see feedback here.</p></div>`;
    grammarPreviewPanel.style.display = 'none';
    grammarCountLabel.textContent = '';
  }
 
  function severityWeight(sev){ return sev === 'high' ? 6 : sev === 'medium' ? 3 : 1; }
 
  function renderGrammarResults(text, analysis){
    const { issues, highlights, wordCount, sentenceCount } = analysis;
 
    if (issues.length === 0){
      grammarResultsPanel.innerHTML = `<div class="clean-state"><div class="badge">✓ Looks clean</div><p>No issues found in ${wordCount} words across ${sentenceCount} sentence${sentenceCount===1?'':'s'}.</p></div>`;
      grammarPreviewPanel.style.display = 'none';
      grammarCountLabel.textContent = '0 issues';
      return;
    }
 
    const penalty = issues.reduce((sum,i) => sum + severityWeight(i.severity), 0);
    const score = Math.max(0, Math.round(100 - (penalty / Math.max(wordCount,1)) * 100));
    const scoreColor = score >= 85 ? 'var(--green)' : score >= 60 ? 'var(--amber)' : 'var(--red)';
 
    const high = issues.filter(i=>i.severity==='high').length;
    const med = issues.filter(i=>i.severity==='medium').length;
    const low = issues.filter(i=>i.severity==='low').length;
    grammarCountLabel.textContent = `${issues.length} issue${issues.length===1?'':'s'}`;
 
    let html = `
      <div class="grammar-score-wrap">
        <div class="grammar-score-ring" style="background:${scoreColor};">${score}</div>
        <div class="grammar-score-meta"><b>Writing score</b>${wordCount} words · ${sentenceCount} sentence${sentenceCount===1?'':'s'} · ${issues.length} issue${issues.length===1?'':'s'} found</div>
      </div>
      <div class="summary-row">
        <div class="summary-chip high"><span class="num">${high}</span><span class="lbl">Serious</span></div>
        <div class="summary-chip medium"><span class="num">${med}</span><span class="lbl">Moderate</span></div>
        <div class="summary-chip low"><span class="num">${low}</span><span class="lbl">Minor</span></div>
      </div>
      <div class="issue-list">`;
 
    for (const issue of issues){
      html += `<div class="issue ${issue.severity}">
        <div class="issue-head"><div class="issue-title">${escapeHtml(issue.title)}</div><div class="badge-sev ${issue.severity}">${issue.severity}</div></div>
        <div class="issue-desc">${escapeHtml(issue.description)}</div>
        ${issue.snippet ? `<div class="issue-code"><span class="code">${escapeHtml(issue.snippet)}</span></div>` : ''}
      </div>`;
    }
    html += `</div>`;
    grammarResultsPanel.innerHTML = html;
 
    highlightedText.innerHTML = buildHighlightedHtml(text, highlights);
    grammarPreviewPanel.style.display = '';
  }
 
  function checkGrammar(){
    const text = textInput.value;
    if (!text.trim()){ renderGrammarEmpty(); return; }
    grammarResultsPanel.innerHTML = `<div class="empty-state"><span class="icon">•••</span><p>Checking your writing…</p></div>`;
    setTimeout(() => {
      const analysis = analyzeText(text);
      renderGrammarResults(text, analysis);
    }, 250);
  }
 
  checkBtn.addEventListener('click', checkGrammar);
  document.getElementById('textClearBtn').addEventListener('click', () => { textInput.value=''; renderGrammarEmpty(); });
 
})();
</script>
</body>
</html>
