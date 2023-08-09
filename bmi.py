import streamlit as st
st.header("BMI PROJECT")
weight=st.number_input("Enter your weight in KG",step=0.1)
h=st.number_input("Enter your height in cm")
height=h/100
if st.button("submit"):
   bmi=weight/(height)**2
   st.success(f"your BMI IS {bmi}")