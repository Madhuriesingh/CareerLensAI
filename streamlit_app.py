import streamlit as st
from career_engine import generate_career_advice

st.set_page_config(page_title="CareerLens AI (Offline)", layout="centered")
st.title("🎓 CareerLens AI – Free Personality Analyzer")

user_paragraph = st.text_area("✍️ Write a short paragraph about yourself:")

if st.button("Analyze"):
    if user_paragraph.strip():
        with st.spinner("Analyzing your personality and potential..."):
            response = generate_career_advice(user_paragraph)
            st.markdown(response)
    else:
        st.warning("Please enter a paragraph to get started.")
