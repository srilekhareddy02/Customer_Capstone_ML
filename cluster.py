#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#from sklearn.externals import joblib
import joblib
import pandas as pd
import streamlit as st
#from PIL import Image
#load the model
model = joblib.load('c2.pkl')


#page configuration
st.set_page_config(page_title = 'Customer Behaviour Analysis Web App', layout='centered')
st.title('Customer Behaviour')
#image=Image.open('ca.jpg')
st.image("""https://t4.ftcdn.net/jpg/02/97/85/17/360_F_297851731_apSBHOhfsy62vf9X1CGpH1FcvGHtsHEI.jpg""")

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

