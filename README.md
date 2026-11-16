# **Thames Valley Crime Data Analysis**

## README

Thames Valley Police crime data analysis, October 2023 to September 2026.

---

## Context

Thames Valley Police cover 13 areas across the region, and each month they record thousands of crimes. With limited officers, budget and time, they need to know where to target these resources to work effectively.
To guide them, they need to know which crimes are the most common, where they happen, and if certain times of the year are busier than others.

This project analyses 36 months of street-level crime data from October 2023 to September 2026, to give the police a clearer picture of crime across the Thames Valley. The aim is to help them decide where to focus patrols, and when to run awareness campaigns, for example around the months when particular crimes peak.

***The goal:*** Turn a large set of monthly crime records into clear, usable findings, and test whether future monthly crime levels can be predicted so that planning can be based on evidence rather than guesswork.

***The end user:*** Would be police planners or a decision-maker, none of which being a data specialist. That is why the findings will need to be presented in a simple interactive dashboard, where they can filter by area, crime type, and time period to see what the data shows for themselves.

---

## Problem Statement

A key decision maker for the Thames Valley Police is trying to decide where and when to focus resources, with a view of reducing crime in the region.
They are finding it hard to see crime patterns across 13 areas that the force operats in, over the 36 months of basic crime data that they have, and 592,926 crimes having been input in the raw crime data in that time - which makes planning feel like guesswork. ***Can we Help?***

---

## Dataset

**Data Source:** [Thames Valley Police street-level crime data](https://data.police.uk/data/)

**Size - Raw Data** is comprised of 36 monthly CSV files saved in `../data/raw`. There are

**Size - Cleaned Data**

---

## Key Analytical Questions

1. Which reported crime types are the most common across the Thames Valley?
2. How does crime differ between the 13 areas?
3. Has the number of crimes risen or fallen between October 2023 and September 2026?
4. Is there a seasonal pattern, and if so is the difference between summer and winter statistically different?
5. Can monthly crime counts be predicted for an area and crime type, if so which model does it best?

---

## Tools and Technology Used

**Python** - As the programming language (Version 3.12.8)

**VS Code** - As the Integrated Development Environment (IDE)

**Jupyter Notebooks** - As the working environment

**Git/GitHub** - For version control

**Pandas and NumPy** - For cleaning, filtering, and organising data

**Matplotlib, Seaborn & Plotly** - For visualisations ##### CHECK WHICH I HAVE USED #####

**SciPy** - For statistical testing of the seasonal pattern (Question 4)

**Streamlit** - To create the interactive dashboard

**Heroku** - For hosting the dashboard

**Scikit-learn** - For building and evaluating ML models for predicting crime counts (Question 5)

---

## AI Use

While these AI tools were used to support development and brainstorming, the core design, structure, and development of the project are my own. Where AI suggestions or outputs were given, I personally reviewed, adapted and implemented the code to verify its accuracy and to ensure that it aligned with the overall goals of the project.

**AI - Google Gemini** - Initial discussion to assess the viability of the project and dataset

**AI - Claude** - Code assistance, data handling, project management, problem solving, and proofreading

**AI - GitHub Copilot** - Assistance with inline code suggestions

---

## How the project is organised

```
thames-valley-crime-insights/
+---data
|   +---clean
|   \---raw             # Containing 36 monthly raw .csv files
|       
\---jupyter_notebooks
|  01_ETL.ipynb         # Loading, cleaning and combining the raw data
+---app.py
+---Procfile
+---requirements.txt
\---README.md
```

---

## Methodology and Data Management

---

## Answers to our Key Analytical Questions

1. Which reported crime types are the most common across the Thames Valley?

   xxxxxxxxx
2. How does crime differ between the 13 areas?

   xxxxxxxxx
3. Has the number of crimes risen or fallen between October 2023 and September 2026?

   xxxxxxxxx
4. Is there a seasonal pattern, and if so is the difference between summer and winter statistically different?

   xxxxxxxxx
5. Can monthly crime counts be predicted for an area and crime type, if so which model does it best?

   xxxxxxxxx

---

## Conclusion

---

## Recognised Limitations

---

## Data Compliance and Legal Use

---

## Bugs / Technical Issues Encountered

**ppscore install error**

- **Problem:** Installing ppscore 1.1.0 failed with `ModuleNotFoundError: No module named 'pkg_resources'`.
- **Cause:** ppscore is an older package that relies on a part of setuptools that newer versions have removed.
- **Fix:** Installed an older setuptools with `pip install "setuptools<81" wheel`, then installed ppscore with `pip install --no-build-isolation ppscore==1.1.0`.
- **Note:** ppscore is only used locally for analysis and is removed from `requirements.txt` before deploying to Heroku.
- **AI:** Claude was used to troubleshoot and help resolve this (see AI use section).

---

## How to Run This Project

- Clone this repository to your local machine.
- Create a virtual environment using Python 3.12.8 and activate it.
- Install the older setuptools needed for ppscore, then the required Python packages:

```bash
pip install "setuptools<81" wheel
pip install --no-build-isolation ppscore==1.1.0
pip install -r requirements.txt
```
