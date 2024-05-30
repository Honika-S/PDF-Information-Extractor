import streamlit as st
import pdfminer.high_level
from text_extraction import extract_resume_info
from details import format_resume_info

def main():
    st.title("PDF Information Extractor")
    
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    
    if uploaded_file is not None:
        st.write("### PDF Uploaded Successfully!")
        
        if st.button("Extract Info"):
            text = pdfminer.high_level.extract_text(uploaded_file)
            resume_info = extract_resume_info(text)
            formatted_info = format_resume_info(resume_info)
            st.write("### Extracted Information")
            st.write(formatted_info)

if __name__ == "__main__":
    main()
