import pandas as pd

def transformer(complete_data):
    df = pd.DataFrame(complete_data)
    print(df.head())
    df["origin_country"] = df["origin_country"].apply(', '.join)

    print("Countries with the most number of high rated TV shows")
    print(df["origin_country"].value_counts().head())