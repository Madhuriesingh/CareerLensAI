import streamlit as st
from prompt_engine import generate_career_report

st.set_page_config(page_title="CareerLens AI", layout="centered")
st.title("🎯 CareerLens AI – Find Your Path")

paragraph = st.text_area("Write a short paragraph about yourself:")

if st.button("Generate Report"):
    if paragraph.strip():
        with st.spinner("Analyzing..."):
            report = generate_career_report(paragraph)
            st.markdown(report)
    else:
        st.warning("Please write something to analyze.")
