import numpy as np
import pandas as pd
import streamlit as st
import joblib
from tensorflow.keras.models import load_model

model=load_model("Deep_Model_1.keras")
minMax=joblib.load("minMax.joblib")
x_enc=joblib.load("x_enc.joblib")
x_enc=list(dict.fromkeys(x_enc))

st.set_page_config(
    page_title="Deep_learning_project",
    page_icon="😊",
    layout="wide"
)

st.header("THIS IS BATCH2 DEEP LEARNING PROJECT")
st.write("THIS PROJECT IS FOR PREDICTING SALARY")
st.subheader("THIS DEEP LEARNING MODEL IS TRAINED BY 25 EPOCHS")

age=st.number_input("Age")
gender=st.selectbox("Gender",["Male","Female"])
education=st.selectbox("Education",["Bechalors","Diploma","Masters","High School","PhD"])
experience=st.number_input("Experience",0,40,5)
country=st.selectbox("Country",["USA","UK","India","Canada","Australia"])

if st.button("PREDICT MY SALARY"):
    sample=pd.DataFrame({
        "Age":[age],
        "Gender":[gender],
        "Education":[education],
        "Experience":[experience],
        "Country":[country]
})

sample=pd.get_dummies(sample,columns=["Education","Experience","Country"])
sample=sample.reindex(columns=x_enc,fill_value=0)
sample=minMax.transform(sample)

prediction_salary=model.predict(sample)
st.success(f"THE PREDICTED SALARY IS :{prediction_salary[0][0]:,.2f}")
st.subheader("END OF THE APP")