import pandas as pd
import numpy as np
import pickle
from io import StringIO
from functools import lru_cache

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
    df.drop(columns=['date_'], inplace=True)




# defining categories and numeric columns
def make_predcition(Encoder, model, input_df):
    
 # Put the input dictionary in a dataset
    input_data = pd.DataFrame(input_df)
    col = ['city']
    columns = list(input_data.columns)
    encoded_cat = Encoder.transform(input_data[col])
    encoded_cols = Encoder.get_feature_names()
    encoded_cat_ = pd.DataFrame(encoded_cat, columns=encoded_cols)


    
    # we dropped the categorical encoder column before we concat 
    train_enc = input_data.drop(['city'],axis = 1)
    input_d = pd.concat([train_enc, encoded_cat_], axis=1)
    # print(input_d)

    # # convert input_data to a numpy array before flattening to convert it back to a 2D array
    # input_df= input_d.to_numpy()
    print(model.get_booster().feature_names)
    prediction = model.predict(input_d)
    return prediction