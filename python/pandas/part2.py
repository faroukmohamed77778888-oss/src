
def null_handling_strategy(df, strategy="fill_mean"):
    
    if strategy == "fill_mean":
        mean = df["Customer_Age"].mean()
        df["Customer_Age"] = df["Customer_Age"].fillna(mean)

    elif strategy == "drop":
        df = df.dropna()

    return df


print(null_handling_strategy(df_test))



