import streamlit as st
import pandas as pd

# This path points to the file inside our GitHub repository.
DATA_PATH = "data/gnome_381k_stable_materials.parquet"

@st.cache_data
def load_local_data():
    """
    Loads the pre-processed GNoME data from the local Parquet file.
    This is extremely fast.
    """
    try:
        df = pd.read_parquet(DATA_PATH)
        return df
    except FileNotFoundError:
        st.error(f"CRITICAL ERROR: The data file was not found at '{DATA_PATH}'.")
        return pd.DataFrame()
