import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Header of page
st.header('Gemmy I save your life!!!)

#Sub-header of page
st.subheader('The Residual Values')

# Body paragraph
st.write(
    """
    The Residual Values (RV) model is a model to predict car values for given times. There are several car conditions having
    effects to future prices. In the model, transformed categorical features via One-Hot Encoding and scaled numeric
    features via normalization and polynomial transformer. The core model is used CatBoost regression.
    """
)

st.subheader('To use model prediction, please following below steps:')

st.write(
    """
    1. From the left side of this page, there is an area to input several car conditions. \n
    2. To input car conditions that needed to be predicted. \n
    3. See the results below.
    """
)