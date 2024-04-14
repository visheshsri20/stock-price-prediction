import streamlit as st
import numpy as np
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import webbrowser
from streamlit_option_menu import option_menu


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_bmzarwuq.json")
lottie_coding1= load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_cs6ygtm3.json")


def app():
 image_1 = Image.open("images/Vishesh.jpeg")
 image_2 = Image.open("images/Ritika.jpeg")
 with st.container():
    st.title('WHO WE ARE')
    st.write("We're a duo of passionate undergraduate engineers who believe that independent investors need a better way to analyze and research stocks")
    st.write("This stock prediction platform that doesn't just show you data, it helps you interpret the data in a better way.")
    st.write("Our mission is to help part-time investors and beginners like us, take better long-term investment decisions.")
    
 with st.container():
    left_column, right_column = st.columns([2,3])
       
    with right_column:
        st_lottie(lottie_coding, height=300, key="codin")
    
    st.write("---")
    st.title("Our Team :-")
    st.write("##")
    image1,Text1,image2,Text2,image3,Text3= st.columns((2,2,2,2,2,2))
   
    with image1:
        st.image(image_1)
    with Text1:
        st.subheader("Vishesh Srivastava")
        st.write("GLA University")
        if st.button('Linkdln :link:'):
         url = 'www.linkedin.com/in/vishesh-srivastava-05b98a1b3'
         webbrowser.open_new_tab(url)    
    with image2:
        st.image(image_2)
    with Text2:
        st.subheader("Ritika Pandey")
        st.write("GLA University")
        if st.button(' Linkdln :link:'):
         url = 'www.linkedin.com/in/ritika-pandey-26834921a'
         webbrowser.open_new_tab(url)
     