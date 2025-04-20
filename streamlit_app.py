import streamlit as st
from career_engine import generate_career_report

st.set_page_config(page_title="Clarity Coach – Your Personal Career & Life Analyzer", layout="centered")

st.title("🎯 Clarity Coach")
st.subheader("Get a full personality & career report based on what you write.")

user_input = st.text_area("✍️ Describe yourself, your interests, and your goals (min 3–5 sentences):")

if st.button("🔍 Analyze Me"):
    if user_input.strip():
        with st.spinner("Generating your personalized career report..."):
            report = generate_career_report(user_input)
            st.markdown(report)
    else:
        st.warning("Please enter a paragraph to analyze.")
