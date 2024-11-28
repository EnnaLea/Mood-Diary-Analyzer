import streamlit as st
import glob
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

import plotly.express as px

st.title("Diary Tone")

# leggere una serie di file dalla cartella
filepaths = sorted(glob.glob("notes/*.txt"))

# individuare il mood di ciascun file e raggruppare i mood in positivi e negativi
analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []

for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

# prendere le date per il grafico
dates = [name.strip(".txt").strip("notes/") for name in filepaths]


# visualizzare tramite un grafico i rispettivi mood in base alle giornate
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity, labels={"x": "Dates", "y": "Negativity"})


st.plotly_chart(neg_figure)


