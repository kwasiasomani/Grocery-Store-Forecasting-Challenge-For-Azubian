from fastapi import FastAPI
import uvicorn
from datetime import datetime
from typing import Annotated
import os
import sys
import datetime
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.utils import load_file, make_predcition





# Create an instance of FastAPI
app = FastAPI(debug=True)

# get absolute path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

# set path for ml files
ml_contents_path = os.path.join(DIRPATH, '..', 'assets', 'ml_components', 'toolkit_folder')


ml_contents = load_file(ml_contents_path)

Encoder = ml_contents["OneHotEncoder"]
model = ml_contents["model"]

# Get-ChildItem -Path 'src' -Filter "*.pyc" -Recurse | Remove-Item -Force

# del /s /q src\*.pyc
import datetime

def date_extracts(df):
    # Extract date features
    df['year'] = df['date_'].dt.year
    df['month'] = df['date_'].dt.month
    df['dayofmonth'] = df['date_'].dt.day
    df['dayofweek'] = df['date_'].dt.dayofweek
    df['dayofyear'] = df['date_'].dt.dayofyear
    df['weekofyear'] = df['date_'].dt.weekofyear
    df['quarter'] = df['date_'].dt.quarter
    df['is_month_start'] = df['date_'].dt.is_month_start
    df['is_month_end'] = df['date_'].dt.is_month_end
    df['is_quarter_start'] = df['date_'].dt.is_quarter_start
    df['is_quarter_end'] = df['date_'].dt.is_quarter_end
    df['is_year_start'] = df['date_'].dt.is_year_start
    df['is_year_end'] = df['date_'].dt.is_year_end




@app.get('/')
def root():
    return 'Welcome to the Gorecery Sales Forecasting API'

@app.get('/health')
def check_health():
    return {'status': 'ok'}

@app.post('/predict')
async def predict_sales( store_id: int, category_id: int, onpromotion: int,
                  city: str, store_type: int, cluster: int, date: Annotated[datetime.date, "The date of sales"] = datetime.date.today()):

    input = {
    'store_id':[store_id], 
    'category_id':[category_id], 
    'onpromotion' :[onpromotion],
    'type' : [store_type], 
    'cluster': [cluster],
    'city' : [city]
    }   
    input_data = pd.DataFrame()
 
    # sales = make_predcition(Encoder, model, input)
    # sales_value = float(sales[0])
    return {'sales': 'sales_value'}



if __name__ == "__main__":
    uvicorn.run('app:app', reload=True)







    # def date_extracts(data):
    # data['Year'] = data.index.year
    # data['Month'] = data.index.month
    # data['DayOfMonth'] = data.index.day
    # data['DaysInMonth'] = data.index.days_in_month
    # data['DayOfYear'] = data.index.day_of_year
    # data['DayOfWeek'] = data.index.dayofweek
    # data['Week'] = data.index.isocalendar().week
    # data['Is_weekend'] = np.where(data['DayOfWeek'] > 4, 1, 0)
    # data['Is_month_start'] = data.index.is_month_start.astype(int)
    # data['Is_month_end'] = data.index.is_month_end.astype(int)
    # data['Quarter'] = data.index.quarter
    # data['Is_quarter_start'] = data.index.is_quarter_start.astype(int)
    # data['Is_quarter_end'] = data.index.is_quarter_end.astype(int)
    # data['Is_year_start'] = data.index.is_year_start.astype(int)
    # data['Is_year_end'] = data.index.is_year_end.astype(int)