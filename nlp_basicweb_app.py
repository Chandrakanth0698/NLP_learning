import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
from sentiment_analysis import sentimental_test

st.title("Sentimental Analysis using python nltk library")
text = st.text_area("Enter or paste text here to check the sentiment analysis")
button = st.button("submit", key="submit_button")
if button:
    scores = sentimental_test(text)
    if scores['pos'] > scores['neg']:
        st.info("This is relatively a positive text vibe.")
    else:
        st.info("This text consists of negative vibe. Please be kind!!!")