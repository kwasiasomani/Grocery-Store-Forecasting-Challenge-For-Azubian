# Loading key libraries
import streamlit as st
import os
import pickle
import numpy as np
import pandas as pd
import re
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import requests





# get absolute path and goo two levels up
DIRPATH = DIRPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# get path for app data
app_data_path =os.path.join(DIRPATH,'dev', 'datasets', 'app_data', 'Grocery.csv.crdownload')

# set api endpoint
URL = 'https://bright1-sales-forecasting-api.hf.space'
API_ENDPOINT = '/predict'

# Setting the page configurations
st.set_page_config(page_title = "Prediction Forecasting", layout= "wide", initial_sidebar_state= "auto")

# Setting the page title
st.title("Grocery Store Forecasting Prediction")

# Load the saved data
df = pd.read_csv(app_data_path)

# src\app\images1.jpg
image1 = Image.open('src/app/images1.jpg')
image2 = Image.open('src/app/image 2.jpg')

def make_prediction(store_id, category_id, onpromotion, year,month, dayofmonth, 
                    dayofweek, dayofyear,weekofyear, quarter, is_month_start, 
                    is_quarter_start, is_quarter_end, is_year_start, is_year_end, 
                    year_weekofyear,city, store_type, cluster):
    
    
    parameters = {
    'store_id':int(store_id), 
    'category_id':int(category_id), 
    'onpromotion' :int(onpromotion),
    'year' : int(year), 
    'month' : int(month), 
    'dayofmonth' :int(dayofmonth),
    'dayofweek' : int(dayofweek),
    'dayofyear' : int(dayofyear), 
    'weekofyear' : int(weekofyear), 
    'quarter' : int(quarter),
    'is_month_start' : int(is_month_start),
    'is_month_end' : int(is_month_start), 
    'is_quarter_start' : int(is_quarter_start), 
    'is_quarter_end' : int(is_quarter_end), 
    'is_year_start' : int(is_year_start),
    'is_year_end' : (is_year_end), 
    'year_weekofyear' : int(year_weekofyear),
    'city' : city,
    'store_type' : int(store_type), 
    'cluster': int(cluster),

    } 


    response = requests.post(url=f'{URL}{API_ENDPOINT}', params=parameters)
    sales_value = response.json()['sales']
    sales_value = round(sales_value, 4)
    return sales_value


st.image(image1, width = 700)

st.sidebar.markdown('User Input Details and Information')

store_id= st.sidebar.selectbox('store_id', options = sorted(list(df['store_id'].unique())))
category_id= st.sidebar.selectbox('categegory_id',options = sorted(list(df['category_id'].unique())))
onpromotion= st.sidebar.number_input('onpromotion', min_value= df["onpromotion"].min(), value= df["onpromotion"].min())
year = st.sidebar.selectbox('year', options = sorted(list(df['year'].unique())))
month = st.sidebar.selectbox('month', options = sorted(list(df['month'].unique())))
dayofmonth= st.sidebar.number_input('dayofmonth', min_value= df["dayofmonth"].min(), value= df["dayofmonth"].min())
dayofweek = st.sidebar.number_input('dayofweek', min_value= df["dayofweek"].min(), value= df["dayofweek"].min())
dayofyear = st.sidebar.number_input('dayofyear', min_value= df["dayofyear"].min(), value= df["dayofyear"].min())
weekofyear = st.sidebar.number_input('weekofyear', min_value= df["weekofyear"].min(), value= df["weekofyear"].min())
quarter  = st.sidebar.number_input('quarter', min_value= df["quarter"].min(), value= df["quarter"].min())
is_month_start = st.sidebar.number_input('is_month_start', min_value= df["is_month_start"].min(), value= df["is_month_start"].min())
is_month_end = st.sidebar.number_input('is_month_end', min_value= df["is_month_end"].min(), value= df["is_month_end"].min())
is_quarter_start = st.sidebar.number_input('is_quarter_start', min_value= df["is_quarter_start"].min(), value= df["is_quarter_start"].min())
is_quarter_end = st.sidebar.number_input('is_quarter_end', min_value= df["is_quarter_end"].min(), value= df["is_quarter_end"].min())
is_year_start = st.sidebar.number_input('is_year_start', min_value= df["is_year_start"].min(), value= df["is_year_start"].min())
is_year_end = st.sidebar.number_input('is_year_end', min_value= df["is_year_end"].min(), value= df["is_year_end"].min())
year_weekofyear = st.sidebar.number_input('year_weekofyear', min_value= df["year_weekofyear"].min(), value= df["year_weekofyear"].min())
city =  st.sidebar.selectbox("city:", options= sorted(set(df["city"])))
store_type=  st.sidebar.number_input('type', min_value= df["type"].min(), value= df["type"].min())
cluster = st.sidebar.selectbox('cluster', options = sorted(list(df['cluster'].unique())))



# make prediction 
sales_value = make_prediction(store_id, category_id, onpromotion, year,month, dayofmonth, 
                  dayofweek, dayofyear,weekofyear, quarter, is_month_start, 
                  is_quarter_start, is_quarter_end, is_year_start, is_year_end, 
                  year_weekofyear,city, store_type, cluster)

# get predicted value
if st.button('Predict'):
            st.success('The predicted target is ' + str(sales_value))
  
  