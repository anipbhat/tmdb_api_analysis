import api_get
import write_to_file
import panda_transform
import requests
# Provide your API Key here
api_key = "XXXXXXX"

#TMDB Genres
url = "https://api.themoviedb.org/3/genre/tv/list"
payload = {"api_key": api_key}
response = requests.request("GET", url, params=payload)
genres = response.json()
# TMDB API URL
url = "https://api.themoviedb.org/3/tv/top_rated"

# Fetching data from TMDB
complete_data = api_get.get_data(url, api_key)

# Writing the raw data into a file
write_to_file.write_to_file_fun("data.json", complete_data)

# Using pandas to transform the data and print the countries with the most number of high rated TV shows
panda_transform.transformer(complete_data, genres)
