#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import joblib
import pandas as pd
import streamlit as st
model = joblib.load('c2.pkl')
backgroundColor="#1C6B6B"


#page configuration
st.set_page_config(page_title = 'Customer Behaviour Analysis Web App', layout='centered')
st.title('Customer Behaviour Analysis')
st.image("""https://t4.ftcdn.net/jpg/02/97/85/17/360_F_297851731_apSBHOhfsy62vf9X1CGpH1FcvGHtsHEI.jpg""",use_column_width=True)
st.sidebar.image("""https://hotmart.com/media/2018/04/670x419-Comportamento-do-consumidor_EN.png""",use_column_width=True)
st.sidebar.image("""https://hotmart.com/media/2018/04/670x419-Comportamento-do-consumidor_EN.png""",use_column_width=True)
st.sidebar.image("""https://hotmart.com/media/2018/04/670x419-Comportamento-do-consumidor_EN.png""",use_column_width=True)


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

    
    if st.button("Click to predict"):
        result=segment_customers([[Income,Age,Month_Customer,Total_Spendings,Children]])
    
    st.success(result)
    

if __name__ == '__main__':
        main ()
        


