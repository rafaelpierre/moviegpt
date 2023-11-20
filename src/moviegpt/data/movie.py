"""Helper script to download Wikipedia movie data."""

import httpx
import pandas as pd
import logging

BASE_URL = "https://github.com/prust/wikipedia-movie-data/raw/master/movies-{}s.json"

def get_data(
    start: int = 1960,
    end: int = 2020,
    path: str = "/tmp",
    filename: str = "movies.json"
):
    """Downloads WikiData for movies and saves it as JSON.
    
    Parameters:

    start: Starting year
    end: Ending year
    output_path: Path to where dataset will be saved as JSON.
    """

    logging.info(f"Downloading movie info from {start} to {end}")
    decades = [start + (i * 10) for i in range(int((end-start)/10)+1)]
    list_df = []

    # Makes one GET request for each decade
    for decade in decades:
        response = httpx.get(BASE_URL.format(decade))
        json_movies = response.json()
        df = pd.DataFrame.from_dict(json_movies)
        logging.info(f"DF: {df.head()}")
        list_df.append(df)

    output_df = pd.concat(list_df, axis = 0)
    json_path = f"{path}/{filename}"
    output_df.to_json(json_path, orient = "records")
    
    logging.info(f"Wrote movie data to {json_path}")
    

if __name__ == "__main__":
     get_data()