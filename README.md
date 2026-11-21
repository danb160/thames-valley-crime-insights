# **Thames Valley Crime Data Analysis**

## README

Thames Valley Police crime data analysis, October 2023 to September 2026.
---

## Context

Thames Valley Police cover 13 areas across the region, and each month they record thousands of crimes. With limited officers, budget and time, they need to know where to target these resources to work effectively.
To guide them, they need to know which crimes are the most common, where they happen, and if certain times of the year are busier than others.

This project analyses 36 months of street-level crime data from October 2023 to September 2026, to give the police a clearer picture of crime across the Thames Valley. The aim is to help them decide where to focus patrols, and when to run awareness campaigns, for example around the months when particular crimes peak.

***The goals:*** 
- Turn a large set of monthly crime records into clear, usable findings, and display them in an interactive dashboard.
- To test whether future monthly crime levels can be predicted so that planning can be based on evidence rather than guesswork. The results of

***The end user:*** Would be police planners or key decision-makers, none of which being a data specialist. That is why the findings will need to be presented in a simple interactive dashboard, where they can filter by area and crime type to see what the data shows for themselves.

---

## Problem Statement

A key decision maker for the Thames Valley Police is trying to decide where and when to focus resources, with a view of reducing crime in the region.
They are finding it hard to see crime patterns across 13 areas that the force operate in, over the 36 months of basic crime data that they have, and 592,926 crimes having been input in the raw crime data in that time - which makes planning feel like guesswork. ***Can we Help?***

---

## Dataset

**Data Source:** [DATA.POLICE.UK](https://data.police.uk/data/)

**Size - Raw Data** made up of 36 monthly CSV files saved in `data/raw`.

- 592,926 rows and 12 columns
- 131.9 MB on disk, 375.1 MB in memory

<br>

**Size - Cleaned Data** made up of 3 CSV files saved in `data/clean`.

- `crime_clean.csv` - 579,772 rows and 4 columns, 29.1 MB (one row per crime)
- `crime_summary.csv` - 6,552 rows and 5 columns, 0.3 MB (crime counts per month, season, area and crime type)
- `area_locations.csv` - 13 rows and 3 columns, 423 bytes (centre point of each area)

<br>

`crime_clean.csv` is 78% smaller on disk than the raw data, and uses 106.6 MB in memory instead of 375.1 MB (72% smaller).

This makes using the datasets both faster and more efficient.

---

## Key Analytical Questions

1. Which reported crime types are the most common across the Thames Valley?
2. How does crime differ between the 13 areas?
3. Has the number of crimes risen or fallen between October 2023 and September 2026?
4. Is there a seasonal pattern, and if so is the difference between summer and winter statistically significant?
5. Can monthly crime counts be predicted for an area and crime type, if so which model does it best?

(See below for result)

---

## Hypothesis (Question 4)

**Practical hypothesis:** Crime in the Thames Valley is higher in summer than in winter. If this is true, police resources and awareness campaigns could be planned around the summer peak to mitigate against crime being committed.

**Statistical hypotheses:**

- **Null hypothesis (H0):** there is no difference in average monthly crimes between summer and winter.
- **Alternative hypothesis (H1):** average monthly crimes differ between summer and winter.

(See below for result)

---

## Tools and Technology Used

**[Python](https://www.python.org/)** - As the programming language (Version 3.12.8)

**VS Code** - As the Integrated Development Environment (IDE)

**Jupyter Notebooks** - As the working environment

**[Git](https://git-scm.com/) / [GitHub](https://github.com/)** - For version control

**[Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/)** - For cleaning, filtering, and organising data

**[Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)** - For notebook visualisations

**[Plotly](https://plotly.com/python/) - For interactive dashboard charts

**[Pingouin](https://pingouin-stats.org/)** - For statistical testing (Version 0.5.4)

**[Streamlit](https://streamlit.io/)** - To create the interactive dashboard

**[Heroku](https://www.heroku.com/)** - For hosting the dashboard

**[Scikit-learn](https://scikit-learn.org/)** - For building and evaluating ML models for predicting crime counts (Question 5)

---

## AI Use

AI tools were used to support this project. The project idea, dataset choice, key questions, and analytical decisions are my own.
AI tools helped to plan the notebook structure and suggest code, which I checked, typed, ran and adapted myself where needed. AI helped draft some explanations and findings based on my outputs. Where this happened I checked and edited the wording myself.
Outputs were checked to verify accuracy and to ensure that they aligned with the overall goals of the project. For example, results were checked against earlier notebooks and my lesson notes, and Copilot inline suggestions that changed columns or variables were corrected.

**AI - Google Gemini** - Initial discussion to assess the viability of the project and dataset

**AI - Claude** - Planning the notebook structure, code suggestions, explanations of concepts and methods, project management, problem solving (and bug reporting), assistance in drafting explanations and proofreading.

**AI - GitHub Copilot** - Assistance with inline code suggestions

### Example prompts and how AI supported the project

| Prompt (summarised) | How it helped | My role |
|---|---|---|
| "ppscore fails to install with 'No module named pkg_resources'. How do I fix it?" | Suggested installing an older version of setuptools first. | Applied the fix, confirmed it worked, and recorded it in the Bugs section. |
| "Help me plan Question 3 (has crime risen or fallen?) in small steps." | Suggested a monthly line chart, a comparison of three October–September years, and a crime type comparison. | Decided the yearly comparison and line chart answered the question, and dropped the crime type comparison to fit the deadline (added to Further Development instead). |
| "Check my findings match my outputs." | Pointed out typos and wording that didn't match the figures. | Questioned figures that hadn't been printed (e.g. "595 fewer crimes"), added code so every number came from an output, and chose 3 decimal places to show two similar figures were actually different. |
| "Review my AI use section." | Suggested clearer wording. | Edited the wording to reflect how the tools were actually used. |

---

## How the project is organised

```
thames-valley-crime-insights/
+---data
|   +---clean                          # 3 cleaned datasets (see Dataset section)
|   \---raw                            # Containing 36 monthly raw .csv files
+---jupyter_notebooks
|   +---01_ETL.ipynb                   # Loading, cleaning and combining the raw data
|   +---02_EDA.ipynb                   # Exploratory data analysis (Questions 1-3 and partly 4)
|   +---03_statistical_testing.ipynb   # Summer vs winter statistical test (Question 4)
|   \---04_modelling.ipynb             # Predicting monthly crime counts (Question 5)
+---app.py                             # Streamlit dashboard
+---Procfile                           # Tells Heroku how to start the dashboard
+---requirements.txt                   # Python packages needed to run this project
\---README.md                          # Project documentation
```

---

## Methodology and Data Management

---

## Answers to our Key Analytical Questions

1. Which reported crime types are the most common across the Thames Valley?
   - **Violence and sexual offences** is by far the most common crime type, with 217,946 crimes recorded (37.59% of all crime). This is more than three times higher than the next highest, **Anti-social behaviour** (60,597, 10.45%).
   - The top 3 crime types (**Violence and sexual offences**, **Anti-social behaviour** and **Shoplifting**) make up 57.85% of all recorded crime over 36 months, which is more than half.
   - The least common crime types are **Possession of weapons** (4,053, 0.7%), **Robbery** (5,886, 1.02%) and **Theft from the person** (6,669, 1.15%). Together they make up only 2.87% of all crime.

<br>

2. How does crime differ between the 13 areas?

   - Crime **does differ** in the 13 areas in two main ways in **how much** and **which types** make up the biggest share.
  
   - **Buckinghamshire** (18.61%) and **Milton Keynes** (15.57%) record the most crime. **West Oxfordshire** (3.04%) and **South Oxfordshire** (3.85%) record the least (percentages are each area's share of all Thames Valley crime).
   - **Violence and sexual offences** is the largest everywhere (ranging 32% to 44%).
   - Some crime types stand out in particular areas (as a percentage of that area's total crime):
      - **Shoplifting** in Reading (14%), Oxford (13%) and Cherwell (13%).
      - **Bicycle theft** in Oxford 6% (at least 3 times higher than anywhere else).
      - **Vehicle crime** in Slough and Windsor and Maidenhead (8 to 9%).

   - The busiest areas record the most crime, likely due to them being bigger areas with a higher population, so totals alone are not a truly fair comparison.
   - Looking at the mix shows each area has its own pattern, which could help the police target specific crime types in specific areas.

<br>

3. Has the number of crimes risen or fallen between October 2023 and September 2026?

   - Crime **has fallen very slightly** by 0.307% (595 fewer crimes) from Year 1 to Year 3 (October 2023 to September 2026).
   - It dipped slightly in Year 2 (down by 0.615%), then rose again in Year 3 (up by 0.310%).
   - The change is so small that crime has effectively stayed **level**
   - The monthly line chart shows crime peaks every summer (highest in July) and drops every winter. This suggests changes are mainly seasonal rather than a long-term trend (which is explored in Question 4).
   
<br>

4. Is there a seasonal pattern, and if so is the difference between summer and winter statistically different?

   - Yes, there is a clear **seasonal pattern**. Crime rises from winter through spring, to a peak in summer, then falls through autumn to its lowest point in winter.
   - Average crimes per month: Winter 14,458, Spring 16,335, Summer 17,560, Autumn 16,065.
   - Summer averages 3,102 more crimes per month than winter (21.46% higher).

      Hypothesis Result:
   - As the t-test p-value is less than 0.01 (3.6e-09 = 0.0000000036) which is **less than 0.05** we reject the null hypothesis. The difference between summer and winter crime values ***is*** **statistically significant**, and is unlikely to be down to chance alone (result from `03_statistical_testing.ipynb`).

   - There is a clear **seasonal pattern**. Crime rises from winter through spring, to a peak in summer, then falls through autumn to its lowest point in winter. Summer averages 21.46% more crimes per month than winter (result from `02_EDA.ipynb`)

<br>

5. Can monthly crime counts be predicted for an area and crime type, if so which model does it best?

   xxxxxxxxx

---

## Dashboard

[**Click here to be taken to the dashboard**](https://thames-valley-crime-insights-cb70f6424e20.herokuapp.com/)

A Streamlit dashboard presents the findings of the project for non-technical users, such as police planners or key decision-makers. Users can filter the data by area and crime type to explore the patterns that the data has uncovered for themselves.

**The dashboard is made up of two pages:**

- **Project Summary** - Explains what the project is about, the data used, key questions, and how to use the dashboard.
- **Crime Dashboard** - Sidebar filters for each area and crime type, headline numbers and four interactive charts.

Notes for reading the charts: 
- All charts have hover boxes showing exact numbers, plus the toolbar allowing the user to:
   - Download the plot as .png
   - Zoom in / out
   - Pan
   - Auto-scale
   - View the image full-screen

- Charts 1 and 4 each ignore one filter on purpose. Picking one crime type would leave a single bar on Chart 1, and picking one area would leave a single bubble on Chart 4.

**See below how the filters work on the dashboard**

| Chart | Area filter | Crime filter | Extra |
|---|---|---|---|
| **Headline numbers** | Yes | Yes | |
| **Chart 1** - Crimes by type | Yes | No - always shows all crime types | Tick box to hide Violence and sexual offences |
| **Chart 2** - Crimes per month | Yes | Yes | |
| **Chart 3** - Average crimes per month by season | Yes | Yes | |
| **Chart 4** - Bubble map of crimes by area | No - always shows all 13 areas | Yes | |
---



---

## Recognised Limitations

**From Data Cleaning**

- **Crimes with no location** - 13,132 crimes (2.21%) were removed. Violence and sexual offences, and Drugs are slightly under-counted by area, and Anti-social behaviour slightly over-represented, but the effect is small and does not change which crimes types are most common.
- **Crimes outside Thames Valley** - 22 crimes recorded in Central Bedfordshire, Dacorum, and Basingstoke and Deane were removed, as these are not among the [13 local authorities that make up the Thames Valley Police area](https://www.westberks.gov.uk/article/42710/Police-Area-Returning-Officer-PARO-2024).
- **Possible double counting** - 163 Crime IDs appear more than once (194 extra rows, 0.03%). These were kept, as they are too few to affect the results.

**From the Data**

- **Counts, not rates** - Larger areas naturally have more crime. Adding population data would allow a fairer comparison.
- **Approximate locations** - Crimes are mapped to a nearby point for privacy.
- **Recorded crime only** - Unreported crime is not included, so the real level of some crimes may be higher.
- **Monthly data only** - No day or time, so seasons are based on the month.
- **Three years only** - Each season only appears three times, which limits the trend analysis 

**From the Statistical Testing**
- **Small sample** - Each season only has 9 months of data, which is only a small sample for the t-test.
- **Cause not tested** - The tests show the difference between summer and winter is real, but do not tell us **why** there it happens.

---

## Further Development

- Add ONS data to investigate crimes per 1,000 people instead of as raw counts. This would give a fairer comparison as larger areas such as Buckinghamshire naturally have more reported crime.
- Compare the change in crime type between Year 1 and 3. This would show if some individual crime types rose while others fell, as overall crime stayed level.
- Further statistical testing to compare all four seasons at once by using the **ANOVA** testing method.

---

## Data Compliance and Legal Use

- The datasets used in this project are puplicly available at [data.police.uk](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). The data has been annoymised to protect privacy. The data is published under [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). This licence allows us to copy, publish, distribute, adapt and commercially exploit the data with attribution.

- This is an independent data analysis project for educational purposes. It is not affiliated with, endorsed by, or produced by Thames Valley Police or data.police.uk.

---

## Bugs / Technical Issues Encountered

**ppscore install error**

- **Problem:** Installing ppscore 1.1.0 failed with `ModuleNotFoundError: No module named 'pkg_resources'`.
- **Cause:** ppscore is an older package that relies on a part of setuptools that newer versions have removed.
- **Fix:** Installed an older setuptools with `pip install "setuptools<81" wheel`, then installed ppscore with `pip install --no-build-isolation ppscore==1.1.0`.
- **Note:** ppscore is only used locally for analysis and is removed from `requirements.txt` before deploying to Heroku.
- **AI:** Claude was used to troubleshoot and help resolve this (see AI use section).

**Charts not showing in the notebook**

- **Problem:** The histogram in `02_EDA.ipynb` did not display. Instead the output showed `<Figure 1000x600 with 1 Axes>`.
- **Cause:** Jupyter in VS Code was not set to show Matplotlib charts inside the notebook.
- **Fix:** Added `%matplotlib inline`to the setup cell, then restarted the kernel and ran all cells.
- **AI:** Claude was used to troubleshoot and help resolve this (see AI use section).

**pingouin install error**

- **Problem:** Installing pingouin upgraded numpy, pandas, matplotlib and scikit-learn past the versions in `requirements.txt`, then failed with `OSError: [WinError 5] Access is denied`.
- **Cause:** The latest pingouin (0.7.0) needs newer versions of these packages. The install failed part-way because the notebook kernel and OneDrive were using the files.
- **Fix:** Closed VS Code, deleted the leftover `~` folders in `.venv\Lib\site-packages`, then reinstalled the pinned versions from the terminal and installed an older pingouin with `pip install pingouin==0.5.4 "xarray<2025"`. Checked with `pip check`.
- **Note:** pingouin is only used locally for statistical testing and is removed from `requirements.txt` before deploying to Heroku.
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

---

## Credits and Other Reference Sources

- [13 local authorities that make up the Thames Valley Police area](https://www.westberks.gov.uk/article/42710/Police-Area-Returning-Officer-PARO-2024) - West Berkshire Council - Used to establish the areas that make up Thames Valley Police (`01_ETL.ipynb`)
- Methodology Hub (2026). *Statistical Tests: Types, Uses, and How to Choose*. Retrieved 19 November 2026, from [https://methodologyhub.com/methods/statistics/statistical-tests/](https://methodologyhub.com/methods/statistics/statistical-tests/) - Used to research which statistical test to use (`03_statistical_testing.ipynb`).
- Code Institute lesson materials were used as a learning resource for the methods applied in this project.
- The `MultiPage` class in `app_pages/multi_page.py` was adapted from the Code Institute Streamlit multi-page lesson.
- The Heroku deployment files (`Procfile` and `setup.sh`) follow the Code Institute "Deploy dashboard" guide.
- The general structure of the notebooks and this README is based on my own Reading food hygiene project, which I have adapted and expanded on to suit this project.