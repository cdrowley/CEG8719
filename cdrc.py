from utils import clean_columns
import requests
import pandas as pd
from bs4 import BeautifulSoup
from typing import Optional


def cdrc_login(username: str, password: str) -> Optional[requests.Session]:
    session = requests.Session()

    # access login page / parse for necessary form fields
    login_url = "https://data.cdrc.ac.uk/user"
    login_response = session.get(login_url)
    login_soup = BeautifulSoup(login_response.text, "html.parser")
    form_build_id = login_soup.find("input", {"name": "form_build_id"})["value"]

    # prepare login data
    login_data = {
        "name": username,
        "pass": password,
        "form_build_id": form_build_id,
        "form_id": "user_login",
        "op": "Log in",
    }

    # attempt login & return session if successful
    login_response = session.post(login_url, data=login_data)
    redirect_url = f"https://data.cdrc.ac.uk/users/{username}"
    if login_response.ok and (login_response.url == redirect_url):
        return session


def cdrc_get_metadata(
    source_url: str, sess: requests.Session
) -> Optional[pd.DataFrame]:
    def clean_metadata(df: pd.DataFrame) -> pd.DataFrame:
        return (
            df.set_index("Field")
            .T.reset_index(drop=True)
            .rename(
                columns={
                    "Spatial / Geographical Coverage Location": "spatial_coverage",
                    "Modified": "modified_date",
                    "Public Access Level": "access_level",
                }
            )
            .pipe(clean_columns)
            .assign(
                modified_date=lambda df: df["modified_date"].astype("datetime64[ns]"),
                release_date=lambda df: df["release_date"].astype("datetime64[ns]"),
                dataset=dataset,
            )
        )

    response = sess.get(source_url)
    if response.ok:
        metadata = pd.read_html(response.text)
        if len(metadata) == 1:
            return metadata[0].pipe(clean_metadata)
