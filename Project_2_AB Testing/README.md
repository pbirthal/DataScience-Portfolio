# A/B Test Analysis for E-commerce Website

## Project Overview
This project analyzes the results of an A/B test conducted by an e-commerce website. The goal is to help the company decide whether to implement a new page, keep the old page, or perhaps run the experiment longer to make their decision.

## Key Features
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Hypothesis testing
- Logistic regression analysis

## Libraries Used
- pandas
- numpy
- random
- matplotlib
- statsmodels

## Main Analyses
1. Data Cleaning and Preprocessing
   - Checking for missing values
   - Ensuring proper alignment of treatment/control groups with page versions

2. Probability Analysis
   - Calculating conversion rates for control and treatment groups
   - Comparing observed differences in conversion rates

3. Hypothesis Testing
   - Formulating null and alternative hypotheses
   - Conducting sampling distribution simulation
   - Calculating p-values

4. Regression Analysis
   - Performing logistic regression to assess the impact of the new page
   - Incorporating additional factors (country) into the regression model

## Key Findings
- The initial analysis showed no significant evidence that the new treatment page leads to more conversions than the old page.
- The p-value from the hypothesis test was approximately 0.905, suggesting no statistical significance in favor of the new page.
- Logistic regression analysis, including country as a factor, still showed no significant effect of the new page on conversion rates.

## Data Source
The project uses two main datasets:
1. 'ab_data.csv': Contains user data, including user ID, timestamp, group (control/treatment), landing page, and conversion status.
2. 'countries.csv': Provides country information for users.

## Future Improvements
- Conduct a longer experiment to gather more data
- Analyze other potential factors that might influence conversion rates
- Implement more advanced statistical techniques for deeper insights
