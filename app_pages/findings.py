import streamlit as st


def findings_body():
    """Build the Findings page - answers to key questions. """

    st.write("## Key Findings")
    st.info("What the data shows, October 2023 to September 2026.")

    # Instruct the user to click on the expanders
    st.write("### Click on the questions below to see answers to the Key Questions.")

    # Expander for Question 1
    with st.expander("**1. Which reported crime types are the most common across the Thames Valley?**"):
        st.markdown("""
    - **Violence and sexual offences** is by far the most common crime type, with 217,946 crimes recorded (37.59% of all crime). This is more than three times higher than the next highest, **Anti-social behaviour** (60,597, 10.45%).
    - The top 3 crime types (**Violence and sexual offences**, **Anti-social behaviour** and **Shoplifting**) make up 57.85% of all recorded crime over 36 months, which is more than half.
    - The least common crime types are **Possession of weapons** (4,053, 0.7%), **Robbery** (5,886, 1.02%) and **Theft from the person** (6,669, 1.15%). Together they make up only 2.87% of all crime.
    """)

    # Expander for Question 2
    with st.expander("**2. How does crime differ between the 13 areas?**"):
        st.markdown("""
   - Crime **does differ** in the 13 areas in two main ways in **how much** and **which types** make up the biggest share.
  
   - **Buckinghamshire** (18.61%) and **Milton Keynes** (15.57%) record the most crime. **West Oxfordshire** (3.04%) and **South Oxfordshire** (3.85%) record the least (percentages are each area's share of all Thames Valley crime).
   - **Violence and sexual offences** is the largest everywhere (ranging 32% to 44%).
   - Some crime types stand out in particular areas (as a percentage of that area's total crime):
      - **Shoplifting** in Reading (14%), Oxford (13%) and Cherwell (13%).
      - **Bicycle theft** in Oxford 6% (at least 3 times higher than anywhere else).
      - **Vehicle crime** in Slough and Windsor and Maidenhead (8 to 9%).

   - The busiest areas record the most crime, likely due to them being bigger areas with a higher population, so totals alone are not a truly fair comparison.
   - Looking at the mix shows each area has its own pattern, which could help the police target specific crime types in specific areas.
    """)

    # Expander for Question 3
    with st.expander("**3. Has the number of crimes risen or fallen between October 2023 and September 2026?**"):
        st.markdown("""
   - Crime **has fallen very slightly** by 0.307% (595 fewer crimes) from Year 1 to Year 3 (October 2023 to September 2026).
   - It dipped slightly in Year 2 (down by 0.615%), then rose again in Year 3 (up by 0.310%).
   - The change is so small that crime has effectively stayed **level**.
   - The monthly line chart shows crime peaks every summer (highest in July) and drops every winter. This suggests changes are mainly seasonal rather than a long-term trend (which is explored in Question 4).
    """)

    # Expander for Question 4
    with st.expander("**4. Is there a seasonal pattern, and if so is the difference between summer and winter statistically significant?**"):
        st.markdown("""
   - Yes, there is a clear **seasonal pattern**. Crime rises from winter through spring, to a peak in summer, then falls through autumn to its lowest point in winter.
   - After carrying out a statistical test, we found that the difference between summer and winter crime values ***is*** **statistically significant**, and is unlikely to be down to chance alone.
   - Average crimes per month: Winter 14,458, Spring 16,335, Summer 17,560, Autumn 16,065.
   - Summer averages 3,102 more crimes per month than winter (21.46% higher).
    """)

    # Limitations of the analysis
    st.warning("""

**Limitations**

**From Data Cleaning**
- **Crimes with no location** - 13,132 crimes (2.21%) were removed. Violence and sexual offences, and Drugs are slightly under-counted by area, and Anti-social behaviour slightly over-represented, but the effect is small and does not change which crime types are most common.
- **Crimes outside Thames Valley** - 22 crimes recorded in Central Bedfordshire, Dacorum, and Basingstoke and Deane were removed, as these are not among the [13 local authorities that make up the Thames Valley Police area](https://www.westberks.gov.uk/article/42710/Police-Area-Returning-Officer-PARO-2024).
- **Possible double counting** - 163 Crime IDs appear more than once (194 extra rows, 0.03%). These were kept, as they are too few to affect the results.

**From the Data**
- **Counts, not rates** - Larger areas naturally have more crime. Adding population data would allow a fairer comparison.
- **Approximate locations** - Crimes are mapped to a nearby point for privacy.
- **Recorded crime only** - Unreported crime is not included, so the real level of some crimes may be higher.
- **Monthly data only** - No day or time, so seasons are based on the month.
- **Three years only** - Each season only appears three times, which limits the trend analysis.

**From the Statistical Testing**
- **Small sample** - Each season only has 9 months of data, which is only a small sample for the t-test.
- **Cause not tested** - Statistical testing shows the difference between summer and winter is real, but does not tell us **why** it happens.
""")