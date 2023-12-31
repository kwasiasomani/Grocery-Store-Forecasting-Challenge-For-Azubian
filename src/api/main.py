from fastapi import FastAPI
import uvicorn
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.utils import load_file, make_predcition


# Create an instance of FastAPI
app = FastAPI(debug=True)

# get absolute path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

# set path for ml files
ml_contents_path = os.path.join(DIRPATH, '..', 'assets', 'ml_components', 'toolkit_folder')

#  load mll components 
ml_contents = load_file(ml_contents_path)

# get inidividual components
Encoder = ml_contents["OneHotEncoder"]
model = ml_contents["model"]

#  define api endpoints
#  root
@app.get('/')
def root():
    return 'Welcome to the Gorecery Sales Forecasting API'


#  health
@app.get('/health')
def check_health():
    return {'status': 'ok'}

#  predict 
@app.post('/predict')
async def predict_sales(store_id: int, category_id: int, onpromotion: int, year: int,
                  month: int, dayofmonth: int, dayofweek: int, dayofyear: int,
                  weekofyear: int, quarter: int, is_month_start: int, is_month_end: int, is_quarter_start: int,
                  is_quarter_end: int, is_year_start: int, is_year_end: int, year_weekofyear: int,
                  city: str, store_type: int, cluster: int):

    #  collect all data inputs into a dictionary
    input = {
    'store_id':[store_id], 
    'category_id':[category_id], 
    'onpromotion' :[onpromotion],
    'type' : [store_type], 
    'cluster': [cluster],
    'year' : [year], 
    'month' :[month], 
    'dayofmonth' :[dayofmonth],
    'dayofweek' : [dayofweek],
    'dayofyear' : [dayofyear], 
    'weekofyear' : weekofyear, 
    'quarter' : [quarter], 
    'is_month_start' : [is_month_start],
    'is_month_end' : [is_month_end], 
    'is_quarter_start' : [is_quarter_start], 
    'is_quarter_end' : [is_quarter_end], 
    'is_year_start' : [is_year_start],
    'is_year_end' : [is_year_end], 
    'year_weekofyear' : [year_weekofyear],
    'city' : [city]
    }   

    #  make prediction
    sales = make_predcition(Encoder, model, input)
    #  get sales value
    sales_value = float(sales[0])
    return {'sales': sales_value}



if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
