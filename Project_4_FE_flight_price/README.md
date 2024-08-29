# Flight Price Prediction Project

## Project Overview
This project focuses on predicting flight prices using various features related to flight details. It involves extensive data preprocessing, feature engineering, and preparation for machine learning model implementation.

## Key Features
- Data cleaning and preprocessing
- Feature engineering
- Handling categorical variables
- Preparing data for machine learning models

## Dataset Features
The dataset includes the following attributes:
- Airline
- Source
- Destination
- Route
- Departure Time
- Arrival Time
- Duration
- Total Stops
- Additional Info
- Price
- Date, Month, Year
- Arrival and Departure hours and minutes

## Libraries Used
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn (for encoding)

## Main Steps
1. Data Loading and Initial Exploration
2. Data Cleaning
   - Handling missing values
   - Converting data types
3. Feature Engineering
   - Extracting time-related features
   - Creating duration features
4. Handling Categorical Variables
   - One-hot encoding for categorical features
   - Target guided encoding for certain variables
5. Data Transformation
   - Combining encoded features with numerical features

## Key Transformations
- Extracted hour and minute information from time columns
- Created duration features in hours and minutes
- Encoded categorical variables like Airline, Source, Destination
- Handled 'Total_Stops' feature with ordinal encoding
- Processed 'Additional_Info' feature with one-hot encoding

## Final Dataset
The final dataset is prepared with all numerical features, ready for machine learning model training. It includes encoded categorical features and engineered numerical features.

## Future Work
- Implement machine learning models for price prediction
- Perform feature importance analysis
- Optimize model performance
- Develop a user interface for price prediction

The data is taken from [Kaggle dataset](https://www.kaggle.com/)
## Highlights of the project
1. Transforming the data types
2. Cleaning data and handling missing values
3. Handling categorical values using Target guided encoding.
4. Handling categorical values using One Hot encoding.
5. Data Preprocessing.
