import streamlit as st
from webpages import code_editor as ce
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def pythonx_lesson2():
    st.title("Lesson 2: Create WordClouds in Python")
    st.header(":one: What is WordClouds")
    st.markdown("""
        A word cloud (also known as a tag cloud) is a visual representation of the frequency of words in a given text. The more frequently a word appears in the text, the larger it appears in the word cloud. It is often used as a way to visualize and analyze large amounts of text data, such as social media posts, news articles, and books.
        """)

    st.image("./images/lesson2-wordcloud.png")
    st.markdown("""
        Typically, a word cloud is created by taking a piece of text and analyzing the **frequency** of each word. The words are then arranged in a visual format, such as a cloud shape, with the most frequent words appearing in the largest font size. The words are often arranged in random positions within the cloud, with the exception of a few words which are positioned in the center or given emphasis.
        """)
    st.header(":two: Using wordcloud Package to generate wordcloud image")
    st.markdown("""
        In this example we will learn how to use external package in Python to complete task in a easy way.

        A Python package is a collection of related code files (called modules) that we can use to help with specific tasks, like math, working with data, or creating graphics. These files are organized in folders, making it easier to manage and reuse the code. We can install a package and then use its functions in wer own Python programs. Popular Python packages include NumPy, pandas, and matplotlib.         
        """)
    
    st.markdown("""
        We can put this text into the textbox, then click Analyze, it will generate a wordcloud image for the input text.
        ```
        Python is a programming language that lets you work quickly and integrate systems more effectively. Python is powerful and easy to learn.

        ```
    """)
    text = st.text_area("Please input text to analyze")
    
    if st.button("Analyze"):
        # Create a WordCloud object
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(fig)
