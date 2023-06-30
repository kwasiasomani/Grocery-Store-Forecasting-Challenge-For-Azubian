# Loading key libraries
import streamlit as st
import os
import numpy as np
import pandas as pd

from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import datetime 



# get absolute path and goo two levels up
DIRPATH = DIRPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# set api endpoint
URL = 'https://bright1-sales-forecasting-ap1-2.hf.space'
API_ENDPOINT = '/predict'

# get list/choices for inputs 
CITIES = ['Accra', 'Aflao', 'Akim Oda', 'Akwatia', 'Bekwai', 'Cape coast', 'Elmina,', 'Gbawe', 'Ho', 'Hohoe', 'intampo', 'Koforidua', 'Kumasi', 'Mampong', 'Obuasi', 'Prestea', 'Suhum', 'Tamale', 'Techiman', 'Tema', 'Teshie', 'Winneba']
CLUSTER = [ i for i in range(0, 17)]
STORE_ID = [ i for i in range(1, 55)]
CATEGORY_ID = [ i for i in range(0, 35)]


# Setting the page configurations
st.set_page_config(page_title = "Prediction Forecasting", layout= "wide", initial_sidebar_state= "auto")

# Setting the page title
st.title("Grocery Store Forecasting Prediction")


# src\app\images1.jpg
image1 = Image.open('src/app/images1.jpg')


def make_prediction(store_id, category_id, onpromotion, city, store_type, cluster, date):
    
    
    parameters = {
    'store_id':int(store_id), 
    'category_id':int(category_id), 
    'onpromotion' :int(onpromotion),
    'city' : city,
    'store_type' : int(store_type), 
    'cluster': int(cluster),
    'date_': date,

    } 

    # make a request to the api
    response = requests.post(url=f'{URL}{API_ENDPOINT}', params=parameters)
    
    sales_value = response.json()['sales']

    sales_value = round(sales_value, 4)
    return sales_value


st.image(image1, width = 700)

st.sidebar.markdown('User Input Details and Information')

# Create interface
date= st.sidebar.date_input("Enter the Date",datetime.date(2023, 6, 30))
store_id= st.sidebar.selectbox('Store id', options=STORE_ID)
category_id= st.sidebar.selectbox('categegory_id', options=CATEGORY_ID)
onpromotion= st.sidebar.number_input('onpromotion', step=1)
city =  st.sidebar.selectbox("city:", options= CITIES)
store_type=  st.sidebar.selectbox('type', options=[0, 1, 2, 3, 4])
cluster = st.sidebar.selectbox('cluster', options = CLUSTER )

# make prediction 
sales_value = make_prediction(store_id, category_id, onpromotion,city, store_type, cluster, date)

# get predicted value
if st.sidebar.button('Predict', use_container_width=True, type='primary'):
            st.success('The predicted target is ' + str(sales_value))
  
  