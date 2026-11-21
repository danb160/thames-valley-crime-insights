import streamlit as st


def summary_body():
    """Build the Project Summary page."""

    # Page heading
    st.write("## Project Summary")

    # Short description of the project
    st.info("This project explores street-level crime reported to Thames Valley Police "
            "between October 2023 and September 2026.")

    # Aim of the project
    st.write("The goal of this project is to transform monthly crime records into clear, "
             "usable findings, so that planning can be based on evidence rather than guesswork.")

    # Data source, key questions and how to use the dashboard
    st.markdown("""
#### The data
- **Source:** [DATA.POLICE.UK](https://data.police.uk/data/)
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/),
  which allows the data to be copied, published, distributed, adapted and used commercially with attribution.
- **Privacy:** The data has been anonymised to protect privacy. 
- **Size:** The data consists of 36 months (3 years), 13 areas, 14 crime types and 579,772 reported crimes after cleaning.

#### Key questions
1. Which reported crime types are the most common?
2. How does crime differ between the 13 areas?
3. Has crime risen or fallen over the 36 months?
4. Is there a seasonal pattern, and is the summer vs winter difference significant?

#### How to use this dashboard

**The dashboard is made up of three pages**

- **Project Summary** - Explains what the project is about, the data used, key questions, and how to use the dashboard.
- **Crime Dashboard** - Sidebar filters for each area and crime type, headline numbers and four interactive charts.
- **Key Findings** - Summarises the main insights discovered, and limitations of the analysis.

**Features**
- The charts in the dashboard are interactive and have hover boxes showing exact numbers.
- The toolbar in the top-right of each chart allows you to download, zoom, pan or view it full-screen.
- The sidebar on all pages allow you to change pages.
- The Crime Dashboard page also allows you to filter the data by area and crime type.
""")

    # AI use statement and credit
    st.markdown("**AI use:** Claude was used to help plan this dashboard, suggest and check parts of the code and assist in drafting some labels and descriptions, which I edited. "
                "The page content and results are from my own investigation and I typed, adapted and tested the code. "
                "See project README for more detail.")
    
    # Credit for the multipage class
    st.markdown("**Credit:** The page menu in this dashboard uses a MultiPage class adapted from the Code Institute Streamlit lesson.")

    # Non-endorsement statement
    st.markdown("**This is an independent data analysis project for educational purposes. It is not "
                "affiliated with, endorsed by, or produced by Thames Valley Police or data.police.uk.**")