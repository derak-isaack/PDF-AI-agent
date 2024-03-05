import streamlit as st 
import pandas as pd

def main():
    st.set_page_config(page_title="Ask your PDF")
    st.header('Ask Your PDF')
    
    pdf = st.file_uploader('Upload your PDF', type=['pdf'])

if __name__ =='main':
    main()
