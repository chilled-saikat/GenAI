import pandas as pd
import numpy as np
import joblib
import streamlit as st

model=joblib.load("DataModel.joblib")

st.set_page_config(
    page_title="JISU BATCH1 PROJECT1",
    page_icon="👍",
    layout="wide"
)

st.title("BREAST CANCER DETECTION APP")
st.write("PREDICT WHETHER A TUMOR IS MALIGNANT OR BENIGN")
st.subheader("ENTER YOUR PATIENT DETAILS")


col1 , col2 , col3= st.columns(3)

with col1:
    radius_mean = st.number_input("Radius Mean", 0.0)
    texture_mean = st.number_input("Texture Mean", 0.0)
    perimeter_mean = st.number_input("Perimeter Mean", 0.0)
    area_mean = st.number_input("Area Mean", 0.0)
    smoothness_mean = st.number_input("Smoothness Mean", 0.0)
    compactness_mean = st.number_input("Compactness Mean", 0.0)
    concavity_mean = st.number_input("Concavity Mean", 0.0)
    concave_points_mean = st.number_input("Concave Points Mean", 0.0)
    symmetry_mean = st.number_input("Symmetry Mean", 0.0)
    fractal_dimension_mean = st.number_input("Fractal Dimension Mean", 0.0)

with col2:
    radius_se = st.number_input("Radius SE", 0.0)
    texture_se = st.number_input("Texture SE", 0.0)
    perimeter_se = st.number_input("Perimeter SE", 0.0)
    area_se = st.number_input("Area SE", 0.0)
    smoothness_se = st.number_input("Smoothness SE", 0.0)
    compactness_se = st.number_input("Compactness SE", 0.0)
    concavity_se = st.number_input("Concavity SE", 0.0)
    concave_points_se = st.number_input("Concave Points SE", 0.0)
    symmetry_se = st.number_input("Symmetry SE", 0.0)
    fractal_dimension_se = st.number_input("Fractal Dimension SE", 0.0)

with col3:
    radius_worst = st.number_input("Radius Worst", 0.0)
    texture_worst = st.number_input("Texture Worst", 0.0)
    perimeter_worst = st.number_input("Perimeter Worst", 0.0)
    area_worst = st.number_input("Area Worst", 0.0)
    smoothness_worst = st.number_input("Smoothness Worst", 0.0)
    compactness_worst = st.number_input("Compactness Worst", 0.0)
    concavity_worst = st.number_input("Concavity Worst", 0.0)
    concave_points_worst = st.number_input("Concave Points Worst", 0.0)
    symmetry_worst = st.number_input("Symmetry Worst", 0.0)
    fractal_dimension_worst = st.number_input("Fractal Dimension Worst", 0.0)

if st.button("PREDICT"):
    input_data=np.array([[
        radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
        compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
        radius_se, texture_se, perimeter_se, area_se, smoothness_se,
        compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
        radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
        compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst

    ]])

    prediction=model.predict(input_data)[0]

    st.subheader("RESULT")

    if prediction==0:
        st.error("MALIGNENT TUMOR DETECTED")
    else:
        st.success("BENIGN TUMOR IS DETECTED")

st.markdown("-----------------------------------------------")