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

    st.sidebar.write("---")
    st.sidebar.write("### Filters")

    # Sidebar filters
    area = st.sidebar.selectbox("Select area", area_options)
    crime = st.sidebar.selectbox("Select crime type", crime_options)

    # Name to show in chart titles (to make charts clearer)
    place = "the Thames Valley" if area == "All areas" else area
    
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

    # Chart 1 - Total crimes by crime type (area filtered)
    st.write("---")
    st.write(f"#### Crimes by type for {place}")
    st.write("Reported from October 2023 to September 2026")

    # Option to hide the Violence and sexual offences crime type
    hide_vso = st.checkbox("Hide Violence and sexual offences",
    help="This crime type is much larger than the others. Hiding it makes the "
    "smaller crime types easier to compare.")
    chart_data = area_data.copy()
    if hide_vso:
        chart_data = chart_data[chart_data["Crime type"] != "Violence and sexual offences"]

    # Total crimes by type, smallest to largest
    crime_types = chart_data.groupby("Crime type")["Count"].sum()
    crime_types = crime_types.sort_values(ascending=True).reset_index()

    # Draw the chart
    fig = px.bar(crime_types, x="Count", y="Crime type", orientation="h",
                 color_discrete_sequence=["steelblue"],
                 text_auto=",",
                 labels={"Count": "Number of crimes", "Crime type": ""})

    # Make the chart more readable
    fig.update_traces(textposition="outside", cliponaxis=False)
    fig.update_layout(font={"size": 14, "color": "#333333"},
                      height=500, bargap=0.15,
                      margin={"r": 70, "t": 30})
    fig.update_yaxes(tickfont={"color": "#333333"})
    fig.update_xaxes(tickfont={"color": "#333333"})

    st.plotly_chart(fig, use_container_width=True)