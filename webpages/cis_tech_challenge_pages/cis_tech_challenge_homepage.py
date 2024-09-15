import streamlit as st
import pandas as pd

def cis_tech_challenge_homepage():
    st.title("CIS Tech Challenge (Fall 2024)")
    st.subheader("Ready to Grow Your Tech Skills and Earn Prizes?")
    st.image("./images/cis_tech_challenge_logo.jpg", caption="Generate by ChatGPT", width=300)

    st.markdown("""
        **Who**: Any currently enrolled CIS student at WTAMU’s COB (undergraduate and graduate students)
        
        **What**: A weekly challenge where you will complete free “guided projects” from Coursera’s Career Academy. 
        - Each week you may complete as many guided projects as you wish. The more guided projects you successfully complete, the more chances you have of winning a prize. 
        - Prizes will be awarded 3 times over the semester. 
        - Prize winners will be randomly selected every month in October, November, and December. 

        Guided projects are hands-on learning activities on Coursera that require about an hour to complete, e.g., Introduction to JavaScript, API Testing Using Rest, or Kubernetes to Create Multi-App Clusters with Ingress & Logging. Guided projects provide all the software and virtual machines needed to learn the topic---nothing to install.
        
        For each successful completion of guided projects during the week will equal the number of times your name will be in the drawing for a monthly prize (ex: 6 guided projects completed for the week = 6 times your name is in the drawing). This will continue throughout the duration of the Challenge.

        Coursera “courses” and “professional certifications” are not a part of this CIS Tech Challenge. You may complete Coursera courses and professional certifications for free as a WT student but <span style="color:blue">only the guided projects will count towards prizes </span>. 

        **When**: The Challenge will begin on Week 4 (week of 9/15/24) of the Fall 2024 semester and end during Week 15 (12/5/24) of the Fall semester.

        **Where**: Through Coursera’s online learning platform (email Dr. Brooks at mbrooks@wtamu.edu if you’re interested in accepting this challenge)!

        **Why**: To help CIS students learn hands on skills applicable to numerous industries and for students to earn certificates for placement on LinkedIn and acknowledged on a resume.

        **What to Learn**: There are hundreds of guided projects to choose from! We recommend the following, but you are not limited to just these
        
        **How**: Enroll in and complete your chosen guided projects. When finished, email the pdf certificate of completion or screenshot of your certificate to Dr. Brooks mbrooks@wtamu.edu For prize consideration, your entry will be counted for the week based on the email received date, not the date of the certificate completion.
        
        **Next**: For more information or to join this program, please reach out to Dr. Brooks at mbrooks@wtamu.edu or 806-651-2495
        
         <h3 style="text-align:center"> Recommended Guided Projects </h3>

        | Week  | Beginning Topics | Advance Topics |
        |:--------------:|:-----------|:-------------------|
        | 1 | Design and Develop a Website using Figma and CSS | Securing Cisco Switches with Port Security |
        | 2 | Create a Website with MailChimp | How to Use The IFE-EFE Matrix for Strategic Analysis |
        | 3 | Getting Started with Linux Terminal | Introduction to Docker: Build Your Own Portfolio Site |
        | 4 | Using MySQL Database with PHP | Create IT Diagrams with Lucidchart |
        | 5 | Master The Art of Digital Marketing with Canva | Create a Python Application using PyMongo and MongoDB Database |
        | 6 | Wireshark for Basic Network Security Analysis | Create digital marketing campaign dashboards in Tableau |
        | 7 | How to create a Jira SCRUM project | Data Visualization in Excel: Build an Interactive Dashboard |
        | 8 | Android Programming for Beginners | Mining Quality Prediction Using Machine & Deep Learning |
        | 9 | Create Your First NoSQL Database with MongoDB and Compass | Machine Learning with ChatGPT: Image Classification Model |
        | 10 | Design and Develop a Website using Figma and CSS | Simulation of Inventory Replenishment Using R Simmer |
        | 11 | Configure and Test Basic Network Connectivity | COVID19 Data Visualization Using Python |
        | 12 | Build Your First React Website | Decryption with Python |
        | 13 | Build Your First React Website (Part II) | Exploratory vs Confirmatory data analysis using Python |
        | 14 | Command Line basics in Linux | Communicate UX Research with Empathy Maps in Miro |


        
        """, unsafe_allow_html=True)


    st.markdown("""<h3 style="text-align:center"> Full List of Available Guided Projects </h3>""", unsafe_allow_html=True)

    

    df = pd.read_csv("./files/GuidedProjects.csv", usecols=["Gateway","Role","Guided Project",])
    st.dataframe(df, use_container_width=True, height=500)



    st.markdown("""<h3 style="text-align:center"> Find Projects Based on Job Roles </h3>""", unsafe_allow_html=True)

    default_role_values = sorted(df["Role"].unique())

    selected_role = st.multiselect(label = "Select Role", options=default_role_values)
    

    if selected_role:
        df_result = df.loc[df['Role'].isin(selected_role)]
        st.dataframe(df_result, use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)










    st.write("*This CIS Technology Challenge is co-sponsored by BuffTeks.")
