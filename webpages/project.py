import streamlit as st
import time

def project():
    st.title("BuffTeks Project")
    project_introduction = """
        Faculty-led coding projects to provide IT solutions and support to problems facing local communities as part of an experiential learning effort.
    """
    st.write(project_introduction)
    
    st.divider()

    # Project Gallery
    st.subheader("Project Gallery")
    st.image("./images/CommunityLinkLogo.svg")

    
