import streamlit as st

import streamlit_antd_components as sac

# This doc is used to set up the navigation bar 
# basic structure is:
def navigation_bar():
    # start page is the homepage
    page_label = "Homepage"
    
    with st.sidebar:
        st.image("./images/BuffTeksLogo.png", caption="Building Skills, Crafting Code, Bridging Communities")

        page_label = sac.menu([
            sac.MenuItem('Homepage', icon='house'),
            sac.MenuItem('Outstanding Members', icon='award'),
            sac.MenuItem('BuffTeks Project', icon='bi bi-laptop'),
            sac.MenuItem('BuffTeks Event', icon='calendar-event', children=[
                    sac.MenuItem('CIS Tech Challenge', icon='bi bi-trophy'),
            ]),
            sac.MenuItem('BuffTeks Classroom', icon='book', children=[
                sac.MenuItem('About Classroom', icon='question-circle'),
                sac.MenuItem('PythonX', icon='bi bi-filetype-py', children=[
                    sac.MenuItem('About PythonX', icon='question-circle'),
                    sac.MenuItem('Lesson1', icon='1-square'),
                    sac.MenuItem('Lesson2', icon='2-square'),
                    sac.MenuItem('Lesson3', icon='3-square'),
                    ]),       
            ]),
            sac.MenuItem("Testing", icon='fingerprint'),
            sac.MenuItem(type='divider'),
            sac.MenuItem('Link', type='group', children=[
                sac.MenuItem('Join Us', icon='person-plus', href='https://wtamuuw.az1.qualtrics.com/jfe/form/SV_2boQtKLCptO33HE'),
            ]),

            sac.MenuItem(type='divider'),
            sac.MenuItem("Reference", icon='paperclip'),

        ], open_all=True)
    
    return page_label
    