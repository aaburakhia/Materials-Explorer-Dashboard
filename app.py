import streamlit as st
import pandas as pd
# --- CHANGE #1: We are now importing our new, fast function ---
from src.data_processing import load_local_data

st.set_page_config(
    page_title="Materials Explorer Dashboard",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Materials Explorer Dashboard")
st.write("Exploring Novel Stable Materials from the Official GNoME Paper")

# We can keep the spinner, but the message is updated. It will be very fast.
with st.spinner("Loading processed materials data..."):
    # --- CHANGE #2: We are now calling our new, fast function ---
    df = load_local_data()

st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="**Total Stable Materials**", value=f"{len(df):,}")

with col2:
    most_stable = df['stability_score'].min()
    st.metric(label="**Most Stable Material (eV/atom)**", value=f"{most_stable:.4f}", help="Lower is more stable. 0.0 is perfectly stable.")

with col3:
    avg_formation_energy = df['formation_energy'].mean()
    st.metric(label="**Avg. Formation Energy (eV/atom)**", value=f"{avg_formation_energy:.2f}")

with col4:
    avg_band_gap = df['band_gap'].mean()
    st.metric(label="**Avg. Band Gap (eV)**", value=f"{avg_band_gap:.2f}")

st.markdown("---")

st.subheader("Official GNoME Stable Materials Summary")
st.dataframe(df.head())
