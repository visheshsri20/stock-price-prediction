import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu
from multiapp import MultiApp
from apps import home,contact,about,predict # import your app modules here


app1 = MultiApp()

st.set_page_config(page_title="Stock Market Prediction", page_icon=":bar_chart:", layout="wide")
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
selected = option_menu(
    menu_title=None, 
    options=["Home", "Predict", "Contact Us","About Us"], 
    icons=['house', 'graph-up-arrow', "telephone-fill","file-person"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal")
if selected=="Home":
    app1.add_app("Home", home.app)
if selected=="Contact Us":
    app1.add_app("Contact", contact.app)
if selected=="About Us":
    app1.add_app("About Us", about.app)
if selected=="Predict":
    app1.add_app("Prediction", predict.app)

app1.run()



