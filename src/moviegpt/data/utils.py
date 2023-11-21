import httpx
import logging
import pandas as pd
from tqdm import tqdm

BASE_URL = "https://github.com/prust/wikipedia-movie-data/raw/master/movies-{}s.json"

def get_movies(
    base_url: str = BASE_URL,
    start: int = 1960,
    end: int = 2020
) -> pd.DataFrame:
    """Fetches WikiData for movies.
    
    Parameters:

    start: Starting year
    end: Ending year
    output_path: Path to where dataset will be saved as JSON.
    """

    logging.info(f"Downloading movie info from {start} to {end}")
    logging.info(f"Base URL: {base_url}")
    decades = [start + (i * 10) for i in range(int((end-start)/10)+1)]
    results = []

    # Makes one GET request for each decade
    for decade in tqdm(decades, colour = "cyan"):
        response = httpx.get(url = base_url.format(decade), follow_redirects=True)
        logging.info(f"Response Status: {response.status_code}")
        logging.info(f"Response text: {response.text}")
        movies_json = response.json()
        movies_df = pd.DataFrame.from_dict(movies_json)
        results.append(movies_df)

    return pd.concat(results, axis = 0)