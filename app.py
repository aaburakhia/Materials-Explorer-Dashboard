import streamlit as st
import pandas as pd
# This import MUST be 'load_local_data'
from src.data_processing import load_local_data

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Materials Explorer Dashboard",
    page_icon="🔬",
    layout="wide"
)

# --- LOAD DATA ---
# This call MUST be 'load_local_data()'
df = load_local_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🎛️ Explore & Filter")

# We add a check here in case the dataframe is empty from an error
if not df.empty:
    crystal_systems = ["All"] + sorted(df['crystal_system'].unique().tolist())
    selected_crystal = st.sidebar.selectbox(
        "Filter by Crystal System:",
        crystal_systems
    )
else:
    selected_crystal = "All" # Default value if data fails to load

# --- FILTER THE DATAFRAME ---
if selected_crystal == "All" or df.empty:
    filtered_df = df
else:
    filtered_df = df[df['crystal_system'] == selected_crystal]

# --- MAIN PAGE LAYOUT ---
st.title("🔬 Materials Explorer Dashboard")
st.write("Exploring Novel Stable Materials from the Official GNoME Paper")

# --- DYNAMIC SUMMARY METRICS ---
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

# We add checks here to prevent errors if the dataframe is empty
if not filtered_df.empty:
    with col1:
        st.metric(label="**Materials Found**", value=f"{len(filtered_df):,}")
    with col2:
        most_stable = filtered_df['stability_score'].min()
        st.metric(label="**Most Stable (eV/atom)**", value=f"{most_stable:.4f}", help="Lower is more stable.")
    with col3:
        avg_formation_energy = filtered_df['formation_energy'].mean()
        st.metric(label="**Avg. Formation Energy (eV/atom)**", value=f"{avg_formation_energy:.2f}")
    with col4:
        avg_band_gap = filtered_df['band_gap'].mean()
        st.metric(label="**Avg. Band Gap (eV)**", value=f"{avg_band_gap:.2f}")
else:
    st.error("Data could not be loaded. Please check the logs.")

st.markdown("---")

# --- DISPLAY FILTERED DATA ---
st.subheader(f"Displaying Materials for: {selected_crystal}")
st.dataframe(filtered_df.head())
