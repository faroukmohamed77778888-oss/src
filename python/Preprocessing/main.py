from preprocessing import Read_data_file
from preprocessing import Drop_unnecessary_features
from preprocessing import Check_data_type

from config.config import cols_to_drop


file_path = "data/raw/titanic.csv"

df = Read_data_file(file_path)

if df is not None:

    print("Original Data:")
    print(df.head())

    df = Drop_unnecessary_features(df, cols_to_drop)

    print("Data after removingunnecessary features:")
    print(df.head())

    print("Data Type Report:")
    print(Check_data_type(df))