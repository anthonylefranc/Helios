# Helios: Sunspot and Solar Radiation Prediction

<img src="https://fedtechmagazine.com/sites/fedtechmagazine.com/files/styles/cdw_hero/public/articles/%5Bcdw_tech_site%3Afield_site_shortname%5D/202310/FTQ423_GetSmart_Hero.jpg?itok=2NokdAur"/>


## Introduction

Helios is a final Bootcamp's project aimed at predicting solar activity, specifically focusing on the number of sunspots (SSN) and the solar radio flux (F10.7, measured in SFU) over a 10-year period. Utilizing advanced time series forecasting techniques, including Meta's Prophet model and the Seasonal Autoregressive Integrated Moving Average (SARIMA) model, Helios provides accurate and valuable insights into solar behavior. This project leverages the comprehensive dataset provided by the National Oceanic and Atmospheric Administration (NOAA).
Features

Sunspot Prediction (SSN): Uses Prophet and SARIMA models to forecast the number of sunspots, providing insights into solar magnetic activity.
Solar Radiation Forecast (F10.7): Another instance of the Prophet model predicts the solar radio flux, crucial for understanding solar emissions.
10-Year Forecasting: Long-term predictions offering a decade of foresight into solar activities.
NOAA Dataset Utilization: Employs authoritative and detailed solar activity data from NOAA.

## Requirements

    Python 3.x
    Pandas
    NumPy
    Plotly
    FB Prophet
    Statsmodels (for SARIMA)

## Installation

To set up Helios, follow these steps:

Clone the repository:

bash

    git clone https://github.com/anthonylefranc/helios.git

Install the required Python packages:

    pip install -r requirements.txt

## Usage

To run the prediction models, execute the main notebooks :
- 10_years_ARIMA_model.ipynb
- 10_years_PROPHET_model.ipynb
- 10_years_f10_prophet.ipynb

## Source dataset

The dataset used in Helios is sourced from NOAA's Solar Data Services, encompassing historical records of sunspot numbers and solar flux.
Contributing

## Acknowledgments

-National Oceanic and Atmospheric Administration (NOAA) for providing the solar activity dataset.
- Meta Platforms, Inc. for the Prophet forecasting model.
- The Statsmodels community for the SARIMA model implementation.

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDVjdDN3ZmxwNW1yNzh3Z2htcnV5bDdsY2h5YmdnNmxpaHFqNmdpcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SqNqLkfccvHGw/giphy.gif)https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDVjdDN3ZmxwNW1yNzh3Z2htcnV5bDdsY2h5YmdnNmxpaHFqNmdpcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SqNqLkfccvHGw/giphy.gif" width="100%"/>
