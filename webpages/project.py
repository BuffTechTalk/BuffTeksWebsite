import streamlit as st
import streamlit_antd_components as sac
import time

def project():
    st.title("BuffTeks Project")
    project_introduction = """
        Faculty-led coding projects to provide IT solutions and support to problems facing local communities as part of an experiential learning effort.
    """
    st.write(project_introduction)
    
    st.divider()

    # Project Gallery
    st.header("Project Gallery")
    st.divider()
    
    col_logo, clo_contributors = st.columns(2)
    with col_logo:
        st.image("./images/CommunityLinkLogo.svg")

    with clo_contributors:
        st.markdown("""
            #### Main Contributors:
            - Darrian Lambert
            - Kim Sundblom
            - Jessica Zoll
            """)
    sac.buttons([
            sac.ButtonsItem(label='View Source Code', icon='github',color='#000000', href='https://github.com/wtamu-buffteks/CommunityLink'),
        ], label='', align='left')
    st.markdown("""
        ### Introduction: 

        - The Community Link project is dedicated to efficiently organizing, tracking, and distributing hard goods and monetary contributions in support of non-profit organizations. 

        ### Key Features: 

        - Streamlined Donation Processes: A user-friendly platform designed to simplify and manage donations. 

        - Operational Efficiency: Helping non-profits improve efficiency through automated tracking and organization of resources. 

        - Effective Resource Allocation: Ensuring donations are properly distributed to meet community needs. 

        ### Goal: 
        - Develop software that enables non-profits to track donations, coordinate volunteer efforts, and ensure effective resource distribution. 
        - Support non-profit organizations in maximizing their impact on the local communities they serve 
        - Apply CIS skills to address real challenges, enhancing your portfolio and gaining invaluable professional experience. 
        - Work alongside a diverse team of peers and faculty, broadening knowledge and skills through collaboration. 
        """)
    st.divider()
    st.image("./images/CL3.jpg")
    st.divider()
    st.image("./images/CL2.jpg")
    st.divider()
    st.image("./images/CL1.jpg")
  
    
