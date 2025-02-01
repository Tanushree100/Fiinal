import streamlit as st
import subprocess
import os

# Set page configuration
st.set_page_config(
    page_title="Front_Page",
    page_icon="person",
)

# Main Page
st.markdown("<h1 style='text-align: center; color: WHITE; font-size:20;'>Poly-Patho-Prognosis</h1>", unsafe_allow_html=True)

st.markdown('#')
st.markdown("<h3 style='text-align: left; color: WHITE; font-size:20;'>By :</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.write("Tanushree Dhali:12621001187")
    st.write("Deboleena Ghosh:  12620003058")
    st.write("Prerana Saha:   12620001087")
    st.write("Dipshikha Mondal: 12621001173")
with col2:
    st.write("tanushree.dhali.cse24@heritageit.edu.in")
    st.write("deboleena.ghosh.cse24@heritageit.edu.in")
    st.write("prerana.saha.cse24@heritageit.edu.in")
    st.write("dipshikha.mondal.cse24@heritageit.edu.in")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static.vecteezy.com/system/resources/thumbnails/006/736/873/small_2x/abstract-blue-circuit-digital-background-free-vector.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
col1, col2, col3 = st.columns(3)

with col1:
    pass
with col3:
    pass
with col2:
    # Replace 'file' with the directory path of your Python script
    script_directory = "C:/Users/dcdha/OneDrive/Desktop/Final/"

    # Run app.py when the button is clicked
    if st.button("Prediction System"):
        app_py_path = os.path.join(script_directory, "app.py")
        subprocess.Popen(["streamlit", "run", app_py_path])

