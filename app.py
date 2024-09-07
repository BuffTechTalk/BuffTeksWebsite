import streamlit as st
import webpages as pg
from webpages.navigation import navigation_bar as nv

page_label = nv()

# block for main pages
if page_label == "Homepage":
    pg.home()

elif page_label == "BuffTeks Project":
    pg.project()

elif page_label == "About Classroom":
    pg.classroom()

elif page_label == "BuffTeks Event":
    pg.event()

elif page_label == "Join Us":
    pg.join_us()

# block of PythonX lessons
elif page_label == "About PythonX":
    pg.pythonx_homepage()    
elif page_label == "Lesson1":
    pg.pythonx_lesson1()
elif page_label == "Lesson2":
    pg.pythonx_lesson2()

# block for testing page
elif page_label == "Testing":
    pg.testing()
elif page_label == "Reference":
    pg.reference()