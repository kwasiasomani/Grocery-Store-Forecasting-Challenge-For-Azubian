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


DIRPATH = DIRPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

app_data_path =os.path.join(DIRPATH,'dev', 'datasets', 'app_data', 'Grocery.csv.crdownload')

# set api endpoint
URL = 'https://bright1-sales-forecasting-api.hf.space/'
API_ENDPOINT = 'predict_sales'

# Setting the page configurations
st.set_page_config(page_title = "Prediction Forecasting", layout= "wide", initial_sidebar_state= "auto")

# Setting the page title
st.title("Grocery Store Forecasting Prediction")

# Load the saved data
df = pd.read_csv(app_data_path)


toolkit = "toolkit_folder"
@st.cache_resource
def load_toolkit(filepath = toolkit):
    with open(toolkit, "rb") as file:
        loaded_toolkit = pickle.load(file)
    return loaded_toolkit

def make_prediction(store_id, category_id, onpromotion, year,month, dayofmonth, 
                    dayofweek, dayofyear,weekofyear, quarter, is_month_start, 
                    is_quarter_start, is_quarter_end, is_year_start, is_year_end, 
                    year_weekofyear,city, store_type, cluster):
    
    # (store_id: int, category_id: int, onpromotion: int, year: int,
    #               month: int, dayofmonth: int, dayofweek: int, dayofyear: int,
    #               weekofyear: int, quarter: int, is_month_start: int, is_quarter_start: int,
    #               is_quarter_end: int, is_year_start: int, is_year_end: int, year_weekofyear: int,
    #               city: str, store_type: int, cluster: int):
    
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
    sales_value = response['output']
    sales_value = round(sales_value, 4)
    return sales_value



toolkit = load_toolkit()
Encoder = toolkit["OneHotEncoder"]
model = toolkit["model"]



# main sections of the app
menu = st.sidebar.radio('menu',['Home view','Prediction target'])

if menu == 'Home view':
      st.write('Grocery Store Time Series Forecasting')
      st.image('images1.jpg',width = 450)
      st.write('Graphical representation and Data Overview')
      if st.checkbox('Data Set '):
            st.table(df.head(15))
st.title('Charts')
graph = st.selectbox('Varieties of graphs',['scatter plot','Bar chat','Histogram'])
if graph == 'scatter plot':
      fig,ax = plt.subplots(figsize=(10,5))
      sns.scatterplot(y = 'target',x = 'onpromotion',data = df.iloc[:1000],palette = 'bright',hue = 'city');
      st.pyplot(fig)

if graph == 'Bar chat':
       fig,ax = plt.subplots(figsize=(10,5))
       t = df.groupby("city")["target"].sum().reset_index().sort_values(by="target",ascending=False).iloc[:10]
       sns.barplot(data=t[:20] , y="target", x="city", palette='Blues_d')
       st.pyplot(fig)

if graph == 'Histogram':
        fig,ax = plt.subplots(figsize=(10,5))
        st.write('Target Categories')
        sns.distplot(df.target.iloc[:20], kde=True)
        st.pyplot(fig)
      




if menu == 'Prediction target':
    st.image('image 2.jpg', width = 460)
    
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



#     input_df = {
#             'store_id':[store_id], 
#             'category_id':[category_id], 
#             'onpromotion' :[onpromotion], 
#             'year' : [year], 
#             'month' :[month], 
#             'dayofmonth' :[dayofmonth],
#             'dayofweek' : [dayofweek],
#             'dayofyear' : [dayofyear], 
#             'weekofyear' : weekofyear, 
#             'quarter' : [quarter], 
#             'is_month_start' : [is_month_start],
#             'is_month_end' : [is_month_start], 
#             'is_quarter_start' : [is_quarter_start], 
#             'is_quarter_end' : [is_quarter_end], 
#             'is_year_start' : [is_year_start],
#             'is_year_end' : [is_year_end], 
#             'year_weekofyear' : [year_weekofyear],
#             'city' : [city], 
#             'type' : [store_type], 
#             'cluster': [cluster]
# } 

#  # Put the input dictionary in a dataset
#     input_data = pd.DataFrame(input_df)



# defining categories and numeric columns

    # col = ['city']
    # columns = list(input_data.columns)
    # encoded_cat = Encoder.transform(input_data[col])
    # encoded_cols = Encoder.get_feature_names()
    # encoded_cat_ = pd.DataFrame(encoded_cat, columns=encoded_cols)


    
    # # we dropped the categorical encoder column before we concat 
    # train_enc = input_data.drop(['city'],axis = 1)
    # input_d = pd.concat([train_enc, encoded_cat_], axis=1)

    # # convert input_data to a numpy array before flattening to convert it back to a 2D array
    # input_df= input_d.to_numpy()
    # prediction = model.predict(input_df.flatten().reshape(1, -1))
    

    if st.button('Predict'):
               st.success('The predicted target is ' + str(round(prediction[0],2)))
  
  