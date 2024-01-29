#Meta's Prophet is giving me a mix of different time frquences in its prediction : it gives me monthly prediction (mean monthly) until 2023-11-01, then extrapolate the dataset to make the prediction but on a daily basis, in need to group values by month, apply a mean to them to output a monthly frequence on each value
import pandas as pd
import numpy as np

def group_and_average_by_month(dataframe, timestamp_column):
    # Check if the timestamp column exists in the DataFrame
    if timestamp_column not in dataframe.columns:
        raise ValueError(f"'{timestamp_column}' column not found in the DataFrame")

    # Convert the timestamp column to datetime if not already
    dataframe[timestamp_column] = pd.to_datetime(dataframe[timestamp_column])

    # Filter data where the timestamp is after 2023-11-01
    filtered_df = dataframe[dataframe[timestamp_column] > '2023-11-01']

    # Group by month and calculate the mean for all columns
    grouped_df = filtered_df.groupby(pd.Grouper(key=timestamp_column, freq='M')).mean().reset_index()

    return grouped_df

# # Example usage:
# # grouped_data = group_and_average_by_month(your_dataframe, timestamp_column="ds", cutoff_date="2023-11-01")

def mean_absolute_percentage_error(y_true, y_pred): 
    """Calculates MAPE given y_true and y_pred"""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def classify_sfu_data(df, sfu_column):
    """
    Classifies SFU values in a given column of a DataFrame and adds a new column with the classification.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the SFU data.
    sfu_column (str): The name of the column containing SFU values.

    Returns:
    pandas.DataFrame: The original DataFrame with an added column for classification.
    """

    # Conversion factor from SFU to W/m^2
    sfu_to_wm2 = 2.8 * 10**-13

    # Classification thresholds in W/m^2
    class_thresholds_wm2 = {
        'A': 10**-7,
        'B': 10**-6,
        'C': 10**-5,
        'M': 10**-4,
        'X': float('inf')  # Represents a value greater than the M class threshold
    }

    # Convert the classification thresholds to SFU
    class_thresholds_sfu = {k: v / sfu_to_wm2 for k, v in class_thresholds_wm2.items()}

    # Define a function to classify the F10.7 values
    def classify_value(value):
        for class_name, threshold in class_thresholds_sfu.items():
            if value < threshold:
                return class_name
        return 'Extreme'  # A separate class for values greater than the highest threshold

    # Apply the classification to the specified column
    df[sfu_column + '_class'] = df[sfu_column].apply(classify_value)

    return df

# # Example usage
# classified_data = classify_sfu_data(data.copy(), 'f10.7')
# classified_data.head()

