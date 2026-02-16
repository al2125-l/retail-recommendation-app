import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🛍 AI Retail Personalization Dashboard")

df = pd.read_csv("personalized_offers_for_powerbi.csv")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🎯 Customer Insights",
    "📈 Uplift Analysis",
    "🧠 Explainability"
])

# -------- OVERVIEW --------
with tab1:
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Customers", len(df))
    col2.metric("Avg Offer Probability", round(df["Offer_Probability"].mean(),2))
    col3.metric("Avg Uplift", round(df["Uplift"].mean(),2))

    st.bar_chart(df["Offer_Probability"])

# -------- CUSTOMER INSIGHTS --------
with tab2:
    st.subheader("Customer Segments")
    st.dataframe(df.groupby("Segment").mean(numeric_only=True))

# -------- UPLIFT --------
with tab3:
    st.subheader("Top 10 High Uplift Customers")
    top = df.sort_values("Uplift", ascending=False).head(10)
    st.dataframe(top)

# -------- EXPLAINABILITY --------
with tab4:
    st.subheader("Feature Impact (SHAP Insights)")
    st.dataframe(df[["Customer_ID", "Top_3_Features", "Top_3_SHAP_Values"]])