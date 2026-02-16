import streamlit as st
import pandas as pd

st.title("🛍 Retail Recommendation Dashboard")

st.write("Upload customer data to generate personalized offers.")

uploaded_file = st.file_uploader("Upload CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data")
    st.dataframe(df.head())