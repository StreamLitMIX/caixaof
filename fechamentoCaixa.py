import RequestDrive

import streamlit as st
import tempfile

archive = st.text_input('Nome do arquivo')
arquivo = st.file_uploader('Anexar um arquivo')

if st.button('Enviar'):
    st.text(arquivo)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(arquivo.read())
        temp_file.seek(0)
        temp_file_path = temp_file.name
        st.text(temp_file_path)
    RequestDrive.EnvioDrive(temp_file_path,archive)
	
    