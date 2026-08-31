import pandas as pd


def Read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception:
        print("Could not read the file.")
        return None


def Drop_unnecessary_features(df, cols_to_drop):
    df = df.drop(columns=cols_to_drop, errors="ignore")
    return df


def Check_data_type(df):
    result = pd.DataFrame({
        "Data Type": df.dtypes,
        "Unique Values": df.nunique()
    })

    return result.T