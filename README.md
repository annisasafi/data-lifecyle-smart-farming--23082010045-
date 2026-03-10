

# Smart Farming Soil Moisture Dashboard

## Project Overview

Project ini merupakan penugasan Big Data & IoT pada Smart Farming Dashboard dari Sensor IoT untuk menganalisis data sensor kelembaban tanah (soil moisture) sesuai data yang dipilih dalam konteks kelembaban tanah multi-layer. Data dianalisis untuk memahami kondisi tanah beserta berbagai kedalaman.

## Dataset
Soil Moisture Dataset from Kaggle.
[https://www.kaggle.com/datasets/amirmohammdjalili/soil-moisture-dataset](url)
Features:
- datetime
- moisture0 – moisture4
- irrigation

## Data Processing
Steps performed:
Proccesing & Analysis 
- Data cleaning
1. Checked dataset structure and column consistency
2. Removed unnecessary or duplicate data
3. Ensured correct data types for each column
   
- Handling missing values
1. Identified missing values using data inspection methods
2. Evaluated the impact of missing data on the dataset
3. Ensured the dataset used for analysis contains complete and reliable records

- Datetime formatting
1. Combined time-related columns (year, month, day, hour, minute, second)
2. Converted them into a single **datetime** column
3. Enabled time-based analysis and visualization
  
- Exploratory Data Analysis (EDA)
1. Generated descriptive statistics of the dataset
2. Analyzed distribution of soil moisture values
3. Examined relationships between moisture sensors
4. Identified patterns and trends in the data

- Data Visualization
1. Built interactive visualizations using Streamlit
2. Displayed soil moisture trends over time
3. Visualized correlation between sensors
4. Implemented alert indicators for low moisture levels

## Data Quality Metrics

Accuracy = 1.0 
Completeness = 1.0 
Timeliness = 1.0

## Dashboard Features

The Streamlit dashboard provides several visualizations:

1. Current Soil Moisture gauge
2. Irrigation alert system
3. Moisture Sensor Trend Time Series
4. Sensor correlation heatmap
5. Moisture distribution
6. Average moisture per sensor
7. Moisture Variability
8. Moisture Trend with Threshold
9. Moisture Sensor Scatter Plot
   
## Dashboard Preview

<img width="1278" height="927" alt="image" src="https://github.com/user-attachments/assets/30a68d2d-4790-40a9-bab3-198d184e8881" />


## Deployment

Dashboard available at:
([Streamlit link](https://data-lifecyle-smart-farming-23082010045.streamlit.app/))

## Author
Siti Anisa Safitri [23082010045]
