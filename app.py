import streamlit as st
import pandas as pd
from src.data_processing import load_gnome_data

st.set_page_config(
    page_title="Materials Explorer Dashboard",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Materials Explorer Dashboard")

# Load the data using our new function
# A spinner will show while the data is being loaded for the first time
with st.spinner("Loading materials data for the first time... this may take a moment."):
    df = load_gnome_data()

st.success(f"Successfully loaded {len(df):,} materials! We are ready to build.")

st.write("Here is a small sample of the real data:")
st.dataframe(df.head())
