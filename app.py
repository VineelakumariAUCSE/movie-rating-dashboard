import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# App title
st.title("🎬 Movie Rating Dashboard")

# Load data
data = pd.read_csv("movies.csv")

# Show dataset
st.subheader("Movie Dataset")
st.dataframe(data)

# Genre filter
genre = st.selectbox("Select Genre", ["All"] + list(data["Genre"].unique()))

if genre != "All":
    data = data[data["Genre"] == genre]

# Average rating
st.subheader("⭐ Average Rating")
st.write(round(data["Rating"].mean(), 2))

# Ratings by movie
st.subheader("📊 Ratings by Movie")
fig, ax = plt.subplots()
sns.barplot(x="Rating", y="Movie", data=data, ax=ax)
st.pyplot(fig)

# Ratings by year
st.subheader("📈 Ratings Over Years")
fig2, ax2 = plt.subplots()
sns.lineplot(x="Year", y="Rating", data=data, marker="o", ax=ax2)
st.pyplot(fig2)
