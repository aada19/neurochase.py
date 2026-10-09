import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="NEUROCHASE | Adaptive AI Maze",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.block-container {padding: 0.5rem 1rem 2rem; max-width: 1500px;}
header[data-testid="stHeader"] {background: transparent;}
</style>
""", unsafe_allow_html=True)

html_path = Path(__file__).resolve().parent / "index.html"
if html_path.is_file():
    components.html(html_path.read_text(encoding="utf-8"), height=1250, scrolling=True)
else:
    st.error("Missing index.html beside streamlit_app.py in the repository.")
