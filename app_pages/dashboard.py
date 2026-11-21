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
    st.write("## **Crime Dashboard**")
    st.write("Pick an area and a crime type to filter the data.")

    # Expander with how the filters work
    with st.expander("**How the filters work**"):
        st.markdown(""" Use the sidebar to select an area or crime type and the dashboard will update.

**Which filters affect each chart:**

| Chart | Area filter | Crime filter | Extra |
|---|---|---|---|
| **Headline numbers** | Yes | Yes | |
| **Chart 1** - Crimes by type | Yes | No - always shows all crime types | Tick box to hide Violence and sexual offences |
| **Chart 2** - Crimes per month | Yes | Yes | |
| **Chart 3** - Average crimes per month by season | Yes | Yes | |
| **Chart 4** - Bubble map of crimes by area | No - always shows all 13 areas | Yes | |
        
""")

    # Options for the sidebar filters
    area_options = ["All areas"] + sorted(summary["Area"].unique())
    crime_options = ["All crime types"] + sorted(summary["Crime type"].unique())

    # Labels above the filters in the sidebar
    st.sidebar.write("---")
    st.sidebar.write("### Filters")

    # Sidebar filters
    area = st.sidebar.selectbox("Select area", area_options)
    crime = st.sidebar.selectbox("Select crime type", crime_options)

    # Names to show in chart titles (to make charts clearer)
    place = "the Thames Valley" if area == "All areas" else area
    crime_label = "all crime types" if crime == "All crime types" else crime
    
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

    # Headline numbers for the selection
    total = filtered["Count"].sum()
    monthly_average = total / filtered["Month"].nunique()

    # Show the numbers together
    st.write("---")
    st.write(f"### Headline numbers for {place} ({crime_label})")
    col1, col2 = st.columns(2)
    col1.metric("Total crimes (over 36 months)", f"{total:,}")
    col2.metric("Average crimes per month", f"{monthly_average:,.0f}")

    # Chart 1 - Total crimes by crime type (area filtered)
    st.write("---")
    st.write(f"### Crimes by type for {place}")
    st.write("All crime types reported from October 2023 to September 2026")

    # Option to hide the Violence and sexual offences crime type
    hide_vso = st.checkbox("Hide Violence and sexual offences for this chart",
                            help="This crime type is much larger than the others. "
                                 "Hiding it makes the smaller crime types easier to compare.")
    chart_data = area_data.copy()
    if hide_vso:
        chart_data = chart_data[chart_data["Crime type"] != "Violence and sexual offences"]

    # Total crimes by type, smallest to largest
    crime_types = chart_data.groupby("Crime type")["Count"].sum()
    crime_types = crime_types.sort_values(ascending=True).reset_index()

    # Draw chart 1
    fig = px.bar(crime_types, x="Count", y="Crime type", orientation="h",
                 hover_name="Crime type",
                 hover_data={"Crime type": False},
                 color_discrete_sequence=["steelblue"],
                 text_auto=",",
                 labels={"Count": "Number of crimes", "Crime type": ""})

    # Make the chart more readable
    fig.update_traces(textposition="outside", cliponaxis=False)
    fig.update_layout(font={"size": 14, "color": "#333333"},
                      height=500, bargap=0.15,
                      margin={"r": 70, "t": 30},
                      hoverlabel={"bgcolor": "#E6F1FB",
                                  "font": {"color": "#333333",
                                           "size": 14}})
    
    fig.update_yaxes(tickfont={"color": "#333333"})
    fig.update_xaxes(tickfont={"color": "#333333"}, 
                     title_font={"color": "#333333"}, tickformat=",")

    # Display chart 1
    st.plotly_chart(fig, use_container_width=True)

    # Chart 2 - Total crimes per month (area and crime filtered)
    st.write("---")
    st.write(f"### Crimes per month for {place}")
    st.write(f"{crime_label.capitalize()} reported from October 2023 to September 2026")

    # Total crimes per month
    monthly = filtered.groupby("Month")["Count"].sum().reset_index()

    # Draw chart 2
    fig = px.line(monthly, x="Month", y="Count", markers=True,
                  color_discrete_sequence=["steelblue"],
                  labels={"Count": "Number of crimes", "Month": ""})

    # Make the chart more readable
    fig.update_traces(hovertemplate="<b>%{x|%B %Y}</b><br>"
                                    "Number of crimes=%{y:,}<extra></extra>")
    fig.update_layout(font={"size": 14, "color": "#333333"},
                      height=500, margin={"r": 30, "t": 30},
                      hoverlabel={"bgcolor": "#E6F1FB",
                                  "font": {"color": "#333333",
                                  "size": 14}})
    
    fig.update_yaxes(tickfont={"color": "#333333"}, 
                     title_font={"color": "#333333"}, tickformat=",")
    fig.update_xaxes(tickfont={"color": "#333333"}, 
                     title_font={"color": "#333333"})
    
    # Display chart 2
    st.plotly_chart(fig, use_container_width=True)

    # Chart 3 - Average crimes by month by season (area and crime filtered)(Q4)
    st.write("---")
    st.write(f"### Average crimes per month by season for {place}")
    st.write(f"{crime_label.capitalize()} reported from October 2023 to September 2026")

    # Average crimes per month in each season, in season order (as in 02_EDA)
    season_order = ["Winter", "Spring", "Summer", "Autumn"]
    season_monthly = filtered.groupby(["Month", "Season"])["Count"].sum().reset_index()

    season_average = (season_monthly.groupby("Season")["Count"].mean()
                      .round(0).reindex(season_order).reset_index())

    # Draw chart 3
    fig = px.bar(season_average, x="Season", y="Count",
                 hover_name="Season",
                 hover_data={"Season": False},
                 color_discrete_sequence=["steelblue"], text_auto=",",
                 labels={"Count": "Average crimes per month", "Season": ""})

    # Make the chart more readable
    fig.update_traces(textposition="outside", cliponaxis=False)
    fig.update_layout(font={"size": 14, "color": "#333333"},
                      height=500, bargap=0.3, margin={"r": 30, "t": 40},
                      hoverlabel={"bgcolor": "#E6F1FB",
                                  "font": {"color": "#333333",
                                  "size": 14}})
    
    fig.update_yaxes(tickfont={"color": "#333333"}, 
                     title_font={"color": "#333333"}, tickformat=",")
    fig.update_xaxes(tickfont={"color": "#333333"}, 
                     title_font={"color": "#333333"})

    # Display chart 3
    st.plotly_chart(fig, use_container_width=True)

    # Chart 4 - Crimes by area (bubble map)
    st.write("---")
    st.write(f"### Crimes by area for {crime_label}")
    st.write("Reported from October 2023 to September 2026. "
             "Bigger bubble = more crimes." )

    # Total crimes per area, joined to each area's central location
    areas = crime_data.groupby("Area")["Count"].sum().reset_index()
    area_map = areas.merge(locations, on="Area")

    # Hover information for each bubble
    hover = {"Count": ":,", "Latitude": False, "Longitude": False}

    # Draw chart 4
    fig = px.scatter_mapbox(area_map, lat="Latitude", lon="Longitude", 
                            size="Count",
                            hover_name="Area", hover_data=hover,
                            labels={"Count": "Number of crimes"},
                            size_max=54, zoom=8.3,
                            center={"lat": 51.71, "lon": -1.05},
                            color_discrete_sequence=["steelblue"],
                            mapbox_style="open-street-map")

    # Make the chart more readable
    fig.update_layout(font={"size": 14, "color": "#333333"},
                      height=700, margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      hoverlabel={"bgcolor": "#E6F1FB",
                                  "font": {"color": "#333333",
                                  "size": 14}})
    
    # Display chart 4 (scroll-zoom off - scroll move page not map)
    st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": False})