import streamlit as st
from webpages import code_editor as ce



def pythonx_lesson1():
    st.title("Lesson 1: Introduction to Python")

    st.markdown("# :one: From Idea to Program")

    st.markdown(
        """
            The following chat outlines the basic logic of computer programming. We start with a task that we want the computer to help complete.

            - **Step 1**: The programmer **analyzes reuqirements** to identify the process to complete the task.
            - **Step 2**: The programmer **implements** the identified process in programming code as a computer program.
            - **Step 3**: The programmer **deploys** the program on the computer and let the complete complete the task and give expected outcomes.

            This is a simplified outline of coding (computer programming), and additional steps may be involved depending on the task's complexity and the program.
        """)
    st.image("./images/CodingProcess.png")


    st.markdown("# :two: First Python Program: Hello PythonX!")
    st.markdown("""Now, let's try our first program, which print out "Hello PythonX" on our computer screen with following code:""")
    st.code("""print("Hello PythonX)""")

    # try sample code of hello pythonX
    ce.code_editor(height="150px",editor_label="lesson1-helloworld")

