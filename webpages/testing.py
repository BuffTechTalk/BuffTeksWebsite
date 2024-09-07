import streamlit as st
import subprocess
from webpages import code_editor as ce


def testing():
    st.title("Testing Page")
    ce.code_editor()
    
    # # [Work]code for instering youtube videos
    # video = "https://youtu.be/HluANRwPyNo?feature=shared"
    # st.video(video)
