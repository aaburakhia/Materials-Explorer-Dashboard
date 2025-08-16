import streamlit as st
import pandas as pd

# The path is now a simple local path within our project,
# because the data file is in the repository with the code.
DATA_PATH = "data/gnome_381k_stable_materials.parquet"

@st.cache_data
def load_local_data():
    """
    Loads the pre-processed GNoME data from the local Parquet file.
    This is extremely fast as it involves no downloading.
    """
    try:
        df = pd.read_parquet(DATA_PATH)
        return df
    except FileNotFoundError:
        st.error(f"Error: The data file was not found at '{DATA_PATH}'. Please make sure the file is uploaded to the 'data' folder in the GitHub repository.")
        return pd.DataFrame() # Return an empty DataFrame to prevent a crash
