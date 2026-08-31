
import pandas as pd

def automated_stat_analyzer(df, column_name):
    data = df[column_name]

    if data.dtype == "object":
        return {"Mode": data.mode()[0]}

    mean = data.mean()
    median = data.median()
    std = data.std()

    if mean > median:
        skewed = "Skewed"
    else:
        skewed = "Not Skewed"

    return {
        "Mean": mean,
        "Median": median,
        "Standard Deviation": std,
        "Skewed": skewed
    }


print(automated_stat_analyzer(df_test, "Sales_Amount"))

