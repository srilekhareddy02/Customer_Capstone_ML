#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import joblib
import pandas as pd
import streamlit as st
#from PIL import Image
#load the model
model = joblib.load('c2.pkl')
backgroundColor="#1C6B6B"


#page configuration
st.set_page_config(page_title = 'Customer Behaviour Analysis Web App', layout='centered')
st.title('Customer Behaviour Analysis')
st.image("""https://t4.ftcdn.net/jpg/02/97/85/17/360_F_297851731_apSBHOhfsy62vf9X1CGpH1FcvGHtsHEI.jpg""")
st.sidebar.image("""https://media.istockphoto.com/photos/successful-business-concept-abstract-black-arrow-on-wooden-cubes-picture-id1226770160?k=20&m=1226770160&s=612x612&w=0&h=4K78W7GoQzI6fhLBJkk6BKzbTgFOuwuoSsSkASUuiOo=""")
st.sidebar.image("""https://lapaas.com/wp-content/uploads/2021/03/Consumer-Behaviour-in-hindi-%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE-%E0%A4%B9%E0%A5%8B%E0%A4%A4%E0%A4%BE-%E0%A4%B9%E0%A5%88_-Complete-Guide-In-Hindi.jpg""")
# customer segmentation function
def segment_customers(input_data):
    
    prediction=model.predict(pd.DataFrame(input_data, columns=['Income', 'Age', 'Month_Customer', 'TotalSpendings', 'Children']))
    print(prediction)
    pred_1 = 0
    if prediction == 1:
            pred_1 = 'Highly Active'

    elif prediction == 2:
            pred_1 = 'Moderately Active'

    elif prediction == 3:
            pred_1 = 'Moderately Least'
    else:
        pred_1 = 'Least Active'

    return pred_1

def main():
    
    Income = st.text_input("Type In The Household Income")
    Age = st.slider ( "Select Age", 18, 85 )
    Month_Customer = st.text_input("Type In The Month Customer")
    Total_Spendings = st.text_input("Type In The Total Spendings")
    Children = st.radio ( "Select no.of Children", (0,1,2,3) )
  
    
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Click to predict"):
        result=segment_customers([[Income,Age,Month_Customer,Total_Spendings,Children]])
    
    st.success(result)
    

if __name__ == '__main__':
        main ()
        
# I have kept it very simple, but i can buitify the web app by using html

