import pandas as pd
import numpy as np
import pickle
from io import StringIO
from functools import lru_cache


def return_features():
    features_ = ['store_id', 'category_id', 'onpromotion', 'type', 'cluster', 'year', 'month', 'dayofmonth', 'dayofweek', 'dayofyear', 'weekofyear', 'quarter', 'is_month_start', 'is_month_end', 'is_quarter_start', 'is_quarter_end', 'is_year_start', 'is_year_end', 'year_weekofyear', 'x0_Accra', 'x0_Aflao', 'x0_Akim Oda', 'x0_Akwatia', 'x0_Bekwai', 'x0_Cape coast', 'x0_Elmina,', 'x0_Gbawe', 'x0_Ho', 'x0_Hohoe', 'x0_Kintampo', 'x0_Koforidua', 'x0_Kumasi', 'x0_Mampong', 'x0_Obuasi', 'x0_Prestea', 'x0_Suhum', 'x0_Tamale', 'x0_Techiman', 'x0_Tema', 'x0_Teshie', 'x0_Winneba']
    return features_



@lru_cache(maxsize=100, )
def load_file(filename):
    with open(filename, 'rb') as file: # read file
        contents = pickle.load(file) # load contents of file
    return contents

def date_extracts(df):
    # Extract date features
    df['date_'] = pd.to_datetime(df['date_'], errors='coerce')
    df['year'] = df['date_'].dt.year
    df['month'] = df['date_'].dt.month
    df['dayofmonth'] = df['date_'].dt.day
    df['dayofweek'] = df['date_'].dt.dayofweek
    df['dayofyear'] = df['date_'].dt.dayofyear
    df['weekofyear'] = df['date_'].dt.weekofyear
    df['quarter'] = df['date_'].dt.quarter
    df['is_month_start'] = df['date_'].dt.is_month_start.astype(int)
    df['is_month_end'] = df['date_'].dt.is_month_end.astype(int)
    df['is_quarter_start'] = df['date_'].dt.is_quarter_start.astype(int)
    df['is_quarter_end'] = df['date_'].dt.is_quarter_end.astype(int)
    df['is_year_start'] = df['date_'].dt.is_year_start.astype(int)
    df['is_year_end'] = df['date_'].dt.is_year_end.astype(int)
    df['year_weekofyear'] = ((df['year'] -2017) *100 )+ df['weekofyear']

    df.drop(columns=['date_'], inplace=True)




# defining categories and numeric columns
def make_predcition(Encoder, model, input_df):
    if isinstance(input_df, dict):
        # Put the input dictionary in a dataset
        input_data = pd.DataFrame(input_df)
    
    if isinstance(input_df, pd.DataFrame):
        input_data = input_df
    col = ['city']
    columns = list(input_data.columns)
    encoded_cat = Encoder.transform(input_data[col])
    encoded_cols = Encoder.get_feature_names()
    encoded_cat_ = pd.DataFrame(encoded_cat, columns=encoded_cols)



    
    # we dropped the categorical encoder column before we concat 
    train_enc = input_data.drop(['city'],axis = 1)
    input_d = pd.concat([train_enc, encoded_cat_], axis=1)
    input_d = input_d.reindex(columns=return_features())

    #  get sales values 
    prediction = model.predict(input_d)
    return prediction