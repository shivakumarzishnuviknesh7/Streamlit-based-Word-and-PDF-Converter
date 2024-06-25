
import streamlit as st
from docx import Document
from docx2pdf import convert
from pdf2docx import Converter
import os

st.title("Word to PDF and PDF to Word Converter")

option = st.selectbox("Choose an option:", ("Word to PDF", "PDF to Word"))
uploaded_file = st.file_uploader("Upload a file", type=["docx", "pdf"])

if uploaded_file:
    if option == "Word to PDF" and uploaded_file.name.endswith(".docx"):
        st.write("Converting Word to PDF...")
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        convert(uploaded_file.name)
        st.success("Conversion completed!")
        with open(uploaded_file.name.replace(".docx", ".pdf"), "rb") as f:
            st.download_button("Download PDF", f, file_name=uploaded_file.name.replace(".docx", ".pdf"))

    elif option == "PDF to Word" and uploaded_file.name.endswith(".pdf"):
        st.write("Converting PDF to Word...")
        output_docx = uploaded_file.name.replace(".pdf", ".docx")
        pdf_file_path = os.path.join(".", uploaded_file.name)

        with open(pdf_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        cv = Converter(pdf_file_path)
        cv.convert(output_docx, start=0, end=None)
        cv.close()

        st.success("Conversion completed!")
        with open(output_docx, "rb") as f:
            st.download_button("Download Word Document", f, file_name=output_docx)
    else:
        st.error("Please upload a valid file.")
