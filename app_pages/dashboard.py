import pandas as pd
import plotly.express as px
import streamlit as st


# Load data once and store it in memory
@st.cache_data
def load_data():
    summary = pd.read_csv("data/clean/crime_summary.csv", parse_dates=["Month"])
    locations = pd.read_csv("data/clean/area_locations.csv")
    return summary, locations


def dashboard_body():
    """Build the Crime Dashboard page: filters, headline numbers and charts."""

    # Load the data
    summary, locations = load_data()

    # Page heading and instructions
    st.write("### Crime Dashboard")
    st.write("Pick an area and a crime type to filter the data.")

    # Options for the sidebar filters
    area_options = ["All areas"] + sorted(summary["Area"].unique())
    crime_options = ["All crime types"] + sorted(summary["Crime type"].unique())

    # Sidebar filters
    area = st.sidebar.selectbox("Select area", area_options)
    crime = st.sidebar.selectbox("Select crime type", crime_options)

    # Filtered by area
    area_data = summary.copy()
    if area != "All areas":
        area_data = area_data[area_data["Area"] == area]
    
    # Filtered by crime type
    crime_data = summary.copy()
    if crime != "All crime types":
        crime_data = crime_data[crime_data["Crime type"] == crime]

    # Filtered by both
    filtered = area_data.copy()
    if crime != "All crime types":
        filtered = filtered[filtered["Crime type"] == crime]

    # Headline number for the selection
    total = filtered["Count"].sum()
    monthly_average = total / filtered["Month"].nunique()

    # Show the number together
    col1, col2 = st.columns(2)
    col1.metric("Total crimes", f"{total:,}")
    col2.metric("Average crimes per month", f"{monthly_average:,.0f}")
    