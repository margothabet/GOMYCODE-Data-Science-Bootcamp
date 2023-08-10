import streamlit as st
#import pickle
import sklearn
with open("model_pickle.pkl",'rb') as file:
    ourModel = pickle.load(file)
st.header("IRIS Project")
Sepal_length=st.number_input("Enter Sepal length")
Sepal_Width=st.number_input("Enter Sepal width")
Petal_length=st.number_input("Enter Petal length")
Petal_width=st.number_input("Enter Petal Width")

# Create a dictionary to map class numbers to flower names
class_to_flower = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

if st.button("Submit"):
   predict=ourModel.predict([[Sepal_length,Sepal_Width,Petal_length,Petal_width]])
   st.success(class_to_flower[predict[0]])
