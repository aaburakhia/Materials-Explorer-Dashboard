import streamlit as st
import pandas as pd
from datasets import load_dataset
import re

@st.cache_data
def load_gnome_data():
    """
    This function loads the GNOME dataset from the Hugging Face Hub,
    takes a 200,000-material subset, processes it, and returns a clean
    DataFrame. The @st.cache_data decorator ensures this heavy lifting
    is only done once, making the app fast.
    """
    # 1. Load the raw dataset using streaming to save memory
    full_dataset = load_dataset("materialsproject/gnome", split='train', streaming=True)

    # 2. Take a sizable subset
    subset_size = 200000
    dataset_subset = full_dataset.take(subset_size)
    df = pd.DataFrame(dataset_subset)

    # 3. Clean and engineer features (as planned in our previous steps)
    df = df.copy()
    df.rename(columns={
        'band_gap_ind': 'band_gap',
        'formation_energy_per_atom': 'formation_energy',
        'formula_reduced': 'formula',
        'stability': 'stability_score'
    }, inplace=True)

    required_columns = [
        'material_id', 'formula', 'formation_energy', 'band_gap',
        'density', 'crystal_system', 'stability_score'
    ]
    df = df[required_columns]

    df.dropna(subset=['formation_energy', 'band_gap', 'density', 'formula'], inplace=True)
    df = df[(df['formation_energy'] > -10) & (df['formation_energy'] < 5)]
    df = df[(df['band_gap'] >= 0) & (df['band_gap'] < 10)]
    df = df[df['density'] > 0]

    return df
