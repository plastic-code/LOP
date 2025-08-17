import streamlit as st
from pathlib import Path

st.set_page_config(page_title="KSA LOP Analysis", layout="wide")

st.title("KSA LOP Analysis (Streamlit wrapper)")
st.caption("This loads your existing HTML/JS dashboard inside Streamlit.")

# Read your cleaned HTML file (rename MAIN -> index.html first)
html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8")

# Render the HTML with scripts (Chart.js, Tailwind via CDN)
st.components.v1.html(html, height=1400, scrolling=True)
