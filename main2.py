import streamlit as st
import os

# def file_selector(folder_path='.'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox('Select a file', filenames)
#     return os.path.join(folder_path, selected_filename)

# filename = file_selector()
# st.write('You selected `%s`' % filename)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
	# To read file as bytes:
	bytes_data = uploaded_file.getvalue()
	st.write(bytes_data)