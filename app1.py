import streamlit as st
import re
import time
from typing import List
from dataclasses import dataclass

st.set_page_config(
    page_title="🔍 Bug Detective - Code Analysis Tool",
    page_icon="🐛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    /* BODY & MAIN */
    body {
        background-color: #ffffff;
    }

    [data-testid="stAppViewContainer"] {
        background: #ffffff;
    }

    [data-testid="stSidebar"] {
        background: #f5f5f5;
    }

    /* SCROLLBAR */
    ::-webkit-scrollbar { 
        width: 8px; 
        height: 8px;
    }
    ::-webkit-scrollbar-track { 
        background: #f0f0f0; 
    }
    ::-webkit-scrollbar-thumb { 
        background: #cccccc; 
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover { 
        background: #999999; 
    }

    /* HEADER SECTION */
    .header-container {
        background: #ffffff;
        padding: 2.5rem 2rem;
        color: #000000;
        text-align: center;
        margin: -2rem -2rem 2rem -2rem;
        border-radius: 0;
        border-bottom: 2px solid #e0e0e0;
    }

    .header-container h1 {
        font-size: 2.8rem;
        margin: 0;
        font-weight: 700;
        color: #000000;
        text-shadow: none;
    }

    .header-container p {
        font-size: 1.1rem;
        margin: 0.75rem 0 0;
        color: #555555;
        font-weight: 500;
    }

    /* SECTION TITLE BOX */
    .section-title-box {
        background: #ffffff;
        border: 2px solid #000000;
        padding: 0.75rem 1.25rem;
        border-radius: 8px;
        margin-bottom: 1.25rem;
        display: inline-block;
    }

    .section-title-box h3 {
        margin: 0;
        font-size: 1.2rem;
        font-weight: 700;
        color: #000000;
    }

    /* CARD STYLES */
    .card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.75rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
    }

    .card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
    }

    /* BUG SEVERITY COLORS - LIGHT MODE */
    .bug-high {
        background: #fff5f5;
        border-left: 5px solid #cc0000;
        padding: 1.25rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }

    .bug-high:hover {
        background: #ffe6e6;
        border-left-color: #990000;
    }

    .bug-medium {
        background: #fff9f0;
        border-left: 5px solid #ff8800;
        padding: 1.25rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }

    .bug-medium:hover {
        background: #ffe6cc;
        border-left-color: #cc6600;
    }

    .bug-low {
        background: #f5fff5;
        border-left: 5px solid #00aa00;
        padding: 1.25rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }

    .bug-low:hover {
        background: #e6ffe6;
        border-left-color: #008800;
    }

    .bug-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #000000;
    }

    .bug-description {
        color: #333333;
        margin-bottom: 0.75rem;
        line-height: 1.6;
        font-size: 0.95rem;
    }

    .bug-line {
        background: #f5f5f5;
        color: #000000;
        padding: 0.75rem;
        border-radius: 6px;
        font-family: 'Courier New', monospace;
        font-size: 0.85rem;
        overflow-x: auto;
        margin-top: 0.75rem;
        border: 1px solid #d0d0d0;
    }

    /* LEARNING PATH */
    .learning-step {
        background: #f9f9f9;
        border-left: 5px solid #0066cc;
        padding: 1.25rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        transition: all 0.3s ease;
    }

    .learning-step:hover {
        background: #f0f0f0;
        border-left-color: #004499;
    }

    .step-number {
        background: #0066cc;
        color: #ffffff;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.95rem;
        flex-shrink: 0;
        box-shadow: 0 2px 8px rgba(0, 102, 204, 0.2);
    }

    .step-text {
        color: #000000;
        font-size: 0.95rem;
        line-height: 1.6;
        font-weight: 500;
    }

    /* BUTTONS */
    .stButton > button {
        width: 100%;
        padding: 0.85rem 1.5rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        border: 2px solid #000000 !important;
        background: #ffffff !important;
        color: #000000 !important;
    }

    .stButton > button:hover {
        background: #000000 !important;
        color: #ffffff !important;
        transform: translateY(-2px) !important;
    }

    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* STATISTICS BOX */
    .stats-box {
        background: #ffffff;
        color: #000000;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 2px solid #e0e0e0;
        font-weight: 600;
    }

    .stats-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        display: block;
        color: #000000;
    }

    .stats-label {
        font-size: 0.95rem;
        color: #555555;
    }

    /* TEXT AREA */
    .stTextArea textarea {
        border-radius: 8px !important;
        border: 2px solid #d0d0d0 !important;
        font-family: 'Courier New', monospace !important;
        background-color: #ffffff !important;
        color: #000000 !important;
        font-size: 0.9rem !important;
    }

    .stTextArea textarea:focus {
        border-color: #000000 !important;
        box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.1) !important;
    }

    /* SELECT BOX */
    .stSelectbox {
        margin-bottom: 1rem;
    }

    .stSelectbox > div > div {
        border-radius: 8px;
        border: 2px solid #d0d0d0 !important;
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* EXPANDER */
    .streamlit-expanderHeader {
        background: #f5f5f5 !important;
        border-radius: 8px !important;
        border: 1px solid #d0d0d0 !important;
        color: #000000 !important;
    }

    .streamlit-expanderHeader:hover {
        background: #eeeeee !important;
    }

    /* SUCCESS MESSAGE */
    .stSuccess {
        background: #f0fff0 !important;
        border-left: 5px solid #00aa00 !important;
        border-radius: 8px !important;
        color: #003300 !important;
        border: 1px solid #cceecc !important;
    }

    /* ERROR MESSAGE */
    .stError {
        background: #fff5f5 !important;
        border-left: 5px solid #cc0000 !important;
        border-radius: 8px !important;
        color: #330000 !important;
        border: 1px solid #ffcccc !important;
    }

    /* WARNING MESSAGE */
    .stWarning {
        background: #fff9f0 !important;
        border-left: 5px solid #ff8800 !important;
        border-radius: 8px !important;
        color: #330000 !important;
        border: 1px solid #ffe6cc !important;
    }

    /* INFO MESSAGE */
    .stInfo {
        background: #f0f7ff !important;
        border-left: 5px solid #0066cc !important;
        border-radius: 8px !important;
        color: #003366 !important;
        border: 1px solid #ccddff !important;
    }

    /* MARKDOWN LINKS */
    a {
        color: #0066cc !important;
        text-decoration: none !important;
    }

    a:hover {
        color: #004499 !important;
        text-decoration: underline !important;
    }

    /* DIVIDER */
    hr {
        border-color: #d0d0d0 !important;
    }

    /* TEXT COLOR */
    p, span, div {
        color: #000000;
    }

    /* RESPONSIVE */
    @media (max-width: 768px) {
        .header-container h1 {
            font-size: 2rem;
        }
        .card {
            padding: 1.25rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==================== DATA CLASSES ====================
@dataclass
class BugPattern:
    pattern: str
    severity: str
    title: str
    description: str
    concept: str
    learning: str

@dataclass
class DetectedBug:
    severity: str
    title: str
    description: str
    concept: str
    learning: str
    match: str
    line: int

# ==================== BUG DETECTOR CLASS ====================
class BugDetectorAI:
    def __init__(self):
        self.bug_patterns = {
            'javascript': [
                BugPattern(
                    pattern=r'for\s*\([^;]*;\s*[^<>=!]*<=\s*[^.]*\.length',
                    severity='high',
                    title='Array Index Out of Bounds',
                    description='Using <= with array.length will access undefined element',
                    concept='Array Indexing',
                    learning='Arrays are zero-indexed. Use < instead of <='
                ),
                BugPattern(
                    pattern=r'==\s*null|null\s*==',
                    severity='medium',
                    title='Loose Equality with Null',
                    description='Using == can lead to type coercion issues',
                    concept='Type Coercion',
                    learning='Always use === for strict comparison'
                ),
                BugPattern(
                    pattern=r'var\s+\w+',
                    severity='low',
                    title='Using var Instead of let/const',
                    description='var has function scope and hoisting issues',
                    concept='Variable Declarations',
                    learning='Use let or const for block scope'
                ),
            ],
            'python': [
                BugPattern(
                    pattern=r'except\s*:',
                    severity='high',
                    title='Bare except Clause',
                    description='Catches all exceptions, hiding important errors',
                    concept='Exception Handling',
                    learning='Specify exception types explicitly'
                ),
                BugPattern(
                    pattern=r'==\s*True|True\s*==',
                    severity='medium',
                    title='Explicit True/False Comparison',
                    description='Unnecessary explicit boolean comparison',
                    concept='Boolean Logic',
                    learning='Use truthiness testing instead'
                ),
                BugPattern(
                    pattern=r'print\s*\(',
                    severity='low',
                    title='Debug Print Statements',
                    description='Should use logging instead of print',
                    concept='Debugging',
                    learning='Implement proper logging framework'
                ),
                BugPattern(
                    pattern=r'range\(len\([^)]+\)\)',
                    severity='medium',
                    title='Using range(len()) Pattern',
                    description='Less Pythonic than using enumerate()',
                    concept='Pythonic Code',
                    learning='Use enumerate() for index and value'
                ),
            ],
            'java': [
                BugPattern(
                    pattern=r'==\s*"[^"]*"|"[^"]*"\s*==',
                    severity='high',
                    title='String Comparison with ==',
                    description='Compares references, not content',
                    concept='String Comparison',
                    learning='Use .equals() for string comparison'
                ),
                BugPattern(
                    pattern=r'catch\s*\([^)]*\)\s*\{\s*\}',
                    severity='medium',
                    title='Empty catch Block',
                    description='Empty catch blocks suppress exceptions',
                    concept='Exception Handling',
                    learning='Always handle exceptions properly'
                ),
            ],
            'cpp': [
                BugPattern(
                    pattern=r'delete\s+[^[;\n]*(?!\[\])',
                    severity='high',
                    title='Using delete Instead of delete[]',
                    description='Memory deallocation mismatch',
                    concept='Memory Management',
                    learning='Use delete[] for arrays'
                ),
            ]
        }

        self.learning_paths = {
            'Array Indexing': ['Understand zero-based indexing', 'Practice iterations', 'Learn array methods'],
            'Type Coercion': ['Learn equality operators', 'Study type conversion', 'Practice with types'],
            'Exception Handling': ['Learn exception types', 'Study error propagation', 'Practice logging'],
            'Boolean Logic': ['Understand truthiness', 'Learn operators', 'Study conditionals'],
            'String Comparison': ['Learn comparison methods', 'Study references vs values'],
            'Pythonic Code': ['Learn Python idioms', 'Study comprehensions', 'Practice clean code'],
            'Debugging': ['Learn logging', 'Study debugging tools', 'Practice techniques'],
            'Memory Management': ['Learn allocation', 'Study pointers', 'Practice RAII'],
        }

    def detect_bugs(self, code: str, language: str) -> List[DetectedBug]:
        patterns = self.bug_patterns.get(language, [])
        detected_bugs = []

        for pattern in patterns:
            try:
                matches = re.finditer(pattern.pattern, code, re.MULTILINE)
                for match in matches:
                    line_number = code[:match.start()].count('\n') + 1
                    detected_bugs.append(DetectedBug(
                        severity=pattern.severity,
                        title=pattern.title,
                        description=pattern.description,
                        concept=pattern.concept,
                        learning=pattern.learning,
                        match=match.group(0).strip(),
                        line=line_number
                    ))
            except:
                pass

        return detected_bugs

    def generate_learning_path(self, bugs: List[DetectedBug]) -> List[str]:
        concepts = list(set(bug.concept for bug in bugs))
        learning_steps = []

        for concept in concepts:
            steps = self.learning_paths.get(concept, ['Study fundamentals'])
            learning_steps.extend(steps)

        return list(dict.fromkeys(learning_steps))[:8]

# ==================== MAIN APP ====================
def main():
    if 'bug_detector' not in st.session_state:
        st.session_state.bug_detector = BugDetectorAI()
        st.session_state.analysis_done = False

    # HEADER
    st.markdown("""
    <div class="header-container">
        <h1>🔍 Bug Detective</h1>
        <p>AI-Powered Code Analysis & Learning Assistant</p>
    </div>
    """, unsafe_allow_html=True)

    # SIDEBAR
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        language = st.selectbox(
            "📝 Select Language",
            options=['python', 'javascript', 'java', 'cpp'],
            help="Choose your programming language"
        )

        st.markdown("---")
        
        with st.expander("📖 Quick Guide"):
            st.markdown("""
            **How to use Bug Detective:**
            1. Paste your code in the editor
            2. Click **Analyze Code**
            3. Review detected issues
            4. Follow the learning path
            5. Apply improvements
            """)

        st.markdown("---")
        
        st.markdown("### 📊 About")
        st.info("""
        **Bug Detective** helps you understand and fix code errors with personalized learning paths.
        
        **Supports:** Python, JavaScript, Java, C++
        """)

    # MAIN CONTENT
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        # Title Box
        st.markdown("""
        <div class="section-title-box">
            <h3>💻 Code Editor</h3>
        </div>
        """, unsafe_allow_html=True)

        example_codes = {
            'python': 'def calculate_total(items):\n    for i in range(len(items)):\n        pass\ntry:\n    result = calculate()\nexcept:\n    print("Error")',
            'javascript': 'for (let i = 0; i <= arr.length; i++) {\n    console.log(arr[i]);\n}\nvar x = 10;',
            'java': 'String name1 = "John";\nif (name1 == "John") { }',
            'cpp': 'int* arr = new int[10];\ndelete arr;'
        }

        code_input = st.text_area(
            "Paste your code here:",
            value=example_codes.get(language, ""),
            height=350,
            label_visibility="collapsed"
        )

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            analyze_btn = st.button("🚀 Analyze Code", use_container_width=True, key="analyze")
        with col_btn2:
            clear_btn = st.button("🔄 Clear Code", use_container_width=True, key="clear")

    with col2:
        # Title Box
        st.markdown("""
        <div class="section-title-box">
            <h3>🐛 Analysis Results</h3>
        </div>
        """, unsafe_allow_html=True)

        if analyze_btn and code_input.strip():
            with st.spinner("🔍 Analyzing code..."):
                time.sleep(0.8)
                bugs = st.session_state.bug_detector.detect_bugs(code_input, language)
                st.session_state.analysis_done = True
                st.session_state.last_bugs = bugs
                st.session_state.last_code = code_input

            if not bugs:
                st.success("✅ No bugs found! Great code!")
                st.balloons()
            else:
                # Statistics
                high_count = sum(1 for b in bugs if b.severity == 'high')
                med_count = sum(1 for b in bugs if b.severity == 'medium')
                low_count = sum(1 for b in bugs if b.severity == 'low')

                col_h, col_m, col_l = st.columns(3)
                with col_h:
                    st.markdown(f'''
                    <div class="stats-box" style="border: 2px solid #cc0000;">
                        <span class="stats-number" style="color: #cc0000;">{high_count}</span>
                        <span class="stats-label">High</span>
                    </div>
                    ''', unsafe_allow_html=True)
                with col_m:
                    st.markdown(f'''
                    <div class="stats-box" style="border: 2px solid #ff8800;">
                        <span class="stats-number" style="color: #ff8800;">{med_count}</span>
                        <span class="stats-label">Medium</span>
                    </div>
                    ''', unsafe_allow_html=True)
                with col_l:
                    st.markdown(f'''
                    <div class="stats-box" style="border: 2px solid #00aa00;">
                        <span class="stats-number" style="color: #00aa00;">{low_count}</span>
                        <span class="stats-label">Low</span>
                    </div>
                    ''', unsafe_allow_html=True)

                st.markdown("---")

                # Bugs
                st.markdown("**Detected Issues:**")
                for bug in bugs:
                    severity_class = f"bug-{bug.severity}"
                    st.markdown(f'''
                    <div class="{severity_class}">
                        <div class="bug-title">{bug.title}</div>
                        <div class="bug-description">{bug.description}</div>
                        <div class="bug-line">Line {bug.line}: <code>{bug.match[:60]}</code></div>
                    </div>
                    ''', unsafe_allow_html=True)

        elif not code_input.strip() and not analyze_btn:
            st.info("📝 Paste your code and click 'Analyze Code' to get started!")

    # LEARNING PATH
    if st.session_state.analysis_done and hasattr(st.session_state, 'last_bugs') and st.session_state.last_bugs:
        st.markdown("""
        <div class="section-title-box">
            <h3>📚 Personalized Learning Path</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)

        learning_path = st.session_state.bug_detector.generate_learning_path(st.session_state.last_bugs)

        st.markdown("Follow these steps to improve your coding skills:")
        st.markdown("")

        for i, step in enumerate(learning_path, 1):
            st.markdown(f'''
            <div class="learning-step">
                <div class="step-number">{i}</div>
                <div class="step-text">{step}</div>
            </div>
            ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()