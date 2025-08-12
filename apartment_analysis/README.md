## Introduction

This section of my repository provides a case study done as part of the "Financial Data Analytics with Python" master's course at Martin Luther University Halle-Wittenberg. The study looks into the characteristics that influence the rental costs of shared apartments in Berlin. Furthermore, it investigates the factors that determine how long ads remain active on the "WG-GESUCHT" platform.

## Review

The case study examines advertisements from Berlin that appear on WG-GESUCHT.de. We collected these advertisements and several indicators using web scraping techniques to create the dataset on July 14, 2024. We evaluated this data using Python, Jupyter notebooks, and many libraries to get insights into the shared apartment market and compared our findings to trends in the broader housing market.

### Literature Review 

Before beginning the web scraping, a literature analysis was conducted to investigate the factors influencing the housing market and its associated prices. The findings of this review are described in a separate chapter. This section summarizes the relevant literature and gives basic reference points for the subsequent analysis. Furthermore , To determine how long an advertisement remains online, we use the WG-GESUCHT website's tips for improving ad effectiveness. According to the website, ads with specific qualities tend to fill up quickly. As a result, we view these features as potential indicators of key influencing factors.

### Web scraping

The web scraping part of the codes is online and can be carried out for Berlin any time that the user runs, and it will be updated with the recent advertisements, but because of the IP ban from the WG-GESUCHT website, I only scraped 200 advertisements to get the answer for each part of the project, but the user can increase to 3000 to one part per day.

### Data Analysis

The data analysis and preparation are discussed in the code of the corresponding Jupyter notebook. The data analysis was separated into two categories: simple data analysis and in-depth analysis. In simple data analysis, we use scraped data from the website; however, in in-depth research, we use the geopy module to locate postal codes of advertisements and expand our study.

### Results and Discussion

The data analysis and preparation are discussed in the code of the corresponding Jupyter notebook. Furthermore, the results and interpretation of the regression results are included in the linked Jupyter notebook file.