import streamlit as st
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

nav = st.sidebar.radio("Navigation",["About","Predict"])
df = pd.read_csv('insurance.csv')

if nav=="About":
    st.title("Health Insurance Premium Predictor")
    st.text(" ")
    st.text(" ")
    st.image('health_insurance.jpg',
             width=700)
    paragraph_text ="""
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tilt+Neon&display=swap" rel="stylesheet">
<style>
    p {
       font-family: 'Tilt Neon', sans-serif;
    }
    img {
    max-width: 100%;
    height: auto;
}
</style>
    <p 
    style="text-align: justify;
    ">In today's 
    fast-paced 
    world, 
    staying ahead in the game of life requires not just good health, but also financial security. Health insurance plays a pivotal role in ensuring that you and your family are protected from the financial burden of unexpected medical expenses. However, choosing the right health insurance plan can be a complex and sometimes daunting task. That's where the Health Insurance Premium Predictor comes in – a user-friendly and highly intuitive app designed to empower you with the information you need to make informed decisions about your health insurance coverage.</p>"""
    st.write(paragraph_text,
             unsafe_allow_html=True)


df.replace({'sex':{'male':0,'female':1}},inplace=True)

df.replace({'smoker':{'yes':0,'no':1}},inplace=True)

df.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)


x = df.drop(columns='charges',axis=1)

y = df['charges']

rfr = RandomForestRegressor()

rfr.fit(x,y)

if nav=="Predict":
    st.title("Enter Details")

    age = st.number_input("Age: ",step=1,min_value=0)

    sex = st.radio("Sex",("Male","Female"))

    if (sex == "Male"):
        s=0
    if (sex == "Female"):
        s=1
    bmi = st.number_input("BMI: ",min_value=0)

    children = st.number_input("Number of children: ",step=1,min_value=0)

    smoke = st.radio("Do you smoke",("Yes","No"))

    if (smoke=="Yes"):
        sm = 0
    if (smoke == "No"):
        sm = 1

    region = st.selectbox('Region',('SouthEast','SouthWest','NorthEast','NorthWest'))

    if (region == "SouthEast"):
        reg = 0
    if (region == "SouthWest"):
        reg = 1
    if (region == "NorthEast"):
        reg = 2
    if (region == "NorthWest"):
        reg = 3

    if st.button("Predict"):
        st.subheader("Predicted Premium")
        st.text(rfr.predict([[age,s,bmi,children,sm,reg]]))
    
