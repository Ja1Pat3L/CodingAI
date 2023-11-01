from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
"""
txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )

coding_area=st.text_area("Coding Area")
output=st.text_area("Output")
solution=st.text_area("Solution")
# Just add it after st.sidebar:

with st.sidebar.chat_message("user"):
    a=st.sidebar.text_area("Hello, I am your Coding Companion. How Can I help!!👋",)

st.write(f'You wrote {len(output)} characters.')

st.write(f'You wrote {len(txt)} characters.')