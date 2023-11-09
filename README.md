# Project DBS: Video Game Sales and Stock Ticker Correlation
Project at the Lucerne University of Applied Sciences and Arts(HSLU), for the Database Systems (DBS) module. The primary goal is to analyze and correlate two distinct datasets: video game ratings and the stock performance of game publishing companies.

## Datasets

To achieve the goal, we utilized the following datasets:
- Video Game Sales with Ratings: [Kaggle Dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings)
- Financial Indicators of US Stocks (2014-2018): [Kaggle Dataset](https://www.kaggle.com/cnic92/200-financial-indicators-of-us-stocks-20142018)
- Additional stock data retrieved from [Stock Analysis](https://stockanalysis.com/stocks)  

## Technologies

    MongoDB: For database management and storage.
    Apache Drill: To perform SQL-like queries on non-relational data.
    PyDrill: A Python client for Apache Drill, used to interface with Drill.
    Matplotlib: A Python 2D plotting library used for creating the graphs and charts.

## Results

The result of this project is a set of visualizations that illustrate the relationship between video game ratings and the financial performance of their respective publishers. The graphs indicate both critic scores and user scores plotted against revenue and sales. A linear regression (OLS) line is drawn to show the trend and potential correlation.
![image](https://github.com/theoliver7/hslu-dbs/assets/10463395/fd62c7c4-8eaa-4b4a-a78b-e6195176dc01)
