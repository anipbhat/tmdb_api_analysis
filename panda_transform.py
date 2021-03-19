import pandas as pd


def transformer(complete_data, genres):
    genres_df = pd.DataFrame(genres['genres'])
    print(genres_df.head())
    complete_data_df = pd.DataFrame(complete_data)
    print(complete_data_df.head())
    high_rated_df = complete_data_df
    high_rated_df["origin_country"] = high_rated_df["origin_country"].apply(', '.join)

    print("Countries with the most number of high rated TV shows")
    print(high_rated_df["origin_country"].value_counts().head())

    print("Min-Max Normalized| Best TV shows based on the weighted average of popularity, vote_average and vote_count")
    complete_data_df['weighted_avg'] = ((complete_data_df['popularity'] - complete_data_df['popularity'].min()) / (
                complete_data_df['popularity'].max() - complete_data_df['popularity'].min())
                          + (complete_data_df['vote_average'] - complete_data_df['vote_average'].min()) / (
                                      complete_data_df['vote_average'].max() - complete_data_df['vote_average'].min())
                          + (complete_data_df['vote_count'] - complete_data_df['vote_count'].min()) / (
                                      complete_data_df['vote_count'].max() - complete_data_df['vote_count'].min())) / 3
    print(complete_data_df.sort_values("weighted_avg", ascending=False).head())

    complete_data_df = pd.DataFrame(complete_data)
    print("Z-Score Normalized| Best TV shows based on the weighted average of popularity, vote_average and vote_count")
    complete_data_df['weighted_avg'] = ((complete_data_df['popularity'] - complete_data_df['popularity'].mean()) / (complete_data_df['popularity'].std())
                          + (complete_data_df['vote_average'] - complete_data_df['vote_average'].mean()) / (complete_data_df['vote_average'].std())
                          + (complete_data_df['vote_count'] - complete_data_df['vote_count'].mean()) / (complete_data_df['vote_count'].std())) / 3
    print(complete_data_df.sort_values("weighted_avg", ascending=False).head())