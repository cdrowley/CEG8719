import os
from pathlib import Path
import requests
import pandas as pd


get_filesize_mb = lambda filename: os.path.getsize(filename) / (1024 * 1024)


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (c.strip().lower().replace(" ", "_") for c in df.columns)
    df.columns.name = None
    return df


def download_file(
    url: str,
    destination: str | Path,
    sess: requests.Session = None,
    chunk_size: int = 8192,
) -> bool:
    """Download a file from a URL to a specified destination."""
    if sess is None:
        response = requests.get(url, stream=True)
    else:
        response = sess.get(url, stream=True)

    if response.ok:
        with open(destination, "wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
        return True
    return False
