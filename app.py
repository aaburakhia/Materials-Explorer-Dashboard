import streamlit as st
import pandas as pd
from src.data_processing import load_local_data

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Materials Explorer Dashboard",
    page_icon="🔬",
    layout="wide"
)

# --- LOAD DATA ---
# This now runs instantly thanks to our local file
df = load_local_data()

# --- SIDEBAR FILTERS ---
# st.sidebar creates a new section on the left
st.sidebar.header("🎛️ Explore & Filter")

# Get a list of unique crystal systems from our data.
# We add "All" to the beginning of the list so the user can select everything.
crystal_systems = ["All"] + sorted(df['crystal_system'].unique().tolist())

# Create the interactive dropdown menu in the sidebar
selected_crystal = st.sidebar.selectbox(
    "Filter by Crystal System:",
    crystal_systems
)

# --- FILTER THE DATAFRAME ---
# This is the logic that filters our data based on the user's selection.
if selected_crystal == "All":
    filtered_df = df # If "All" is selected, we use the full dataframe
else:
    filtered_df = df[df['crystal_system'] == selected_crystal] # Otherwise, we filter

# --- MAIN PAGE LAYOUT ---
st.title("🔬 Materials Explorer Dashboard")
st.write("Exploring Novel Stable Materials from the Official GNoME Paper")

# --- SUMMARY METRICS (NOW DYNAMIC!) ---
# Notice these metrics now use 'filtered_df' instead of 'df'.
# This means they will update automatically when the user changes the filter!
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    # This metric now shows the count of materials *found* by the filter
    st.metric(label="**Materials Found**", value=f"{len(filtered_df):,}")

with col2:
    # This metric now shows the stability for the *filtered* materials
    most_stable = filtered_df['stability_score'].min()
    st.metric(label="**Most Stable (eV/atom)**", value=f"{most_stable:.4f}", help="Lower is more stable.")

with col3:
    avg_formation_energy = filtered_df['formation_energy'].mean()
    st.metric(label="**Avg. Formation Energy (eV/atom)**", value=f"{avg_formation_energy:.2f}")

with col4:
    avg_band_gap = filtered_df['band_gap'].mean()
    st.metric(label="**Avg. Band Gap (eV)**", value=f"{avg_band_gap:.2f}")

st.markdown("---")

# --- DISPLAY FILTERED DATA ---
# This table will also update automatically
st.subheader(f"Displaying Materials for: {selected_crystal}")
st.dataframe(filtered_df.head())
