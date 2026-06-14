import streamlit as st
import pandas as pd

st.title("Sales Analytics Dashboard")

df = pd.read_csv("data/sales_data.csv")

st.subheader("Sales Dataset")

st.dataframe(df)

total_sales = df["Sales_Amount"].sum()

st.metric(
    label="Total Sales",
    value=f"${total_sales:,.2f}"
)
region_sales = (
    df.groupby("Region")["Sales_Amount"].sum()
)

st.subheader("Region-wise Sales")

st.bar_chart(region_sales)
category_sales = (
    df.groupby("Product_Category")["Sales_Amount"].sum()
)

st.subheader("Product Category Sales")

st.bar_chart(category_sales)

selected_region = st.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]
    st.subheader("Summary Statistics")

st.write(df.describe())