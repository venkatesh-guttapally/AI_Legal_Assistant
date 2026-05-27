import streamlit as st
from pypdf import PdfReader

from app import analyze_legal_document

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Legal AI Assistant",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("⚖️ Legal AI Assistant")

st.write("Upload a legal PDF and ask questions.")

# =========================
# FILE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "Upload Legal PDF",
    type="pdf"
)

# =========================
# PROCESS PDF
# =========================

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    pdf_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            pdf_text += text

    st.success("PDF uploaded successfully!")

    # =========================
    # USER QUESTION
    # =========================

    user_question = st.text_area(
        "Ask a legal question"
    )

    # =========================
    # BUTTON
    # =========================

    if st.button("Analyze Document"):

        with st.spinner("Analyzing legal document..."):

            result = analyze_legal_document(
                pdf_text,
                user_question
            )

        st.subheader("Legal Analysis")

        st.write(result)