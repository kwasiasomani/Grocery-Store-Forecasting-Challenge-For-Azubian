from fastapi import FastAPI
import uvicorn
from datetime import datetime
from typing import Annotated
import tabulate
import os
import sys
import datetime
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.utils import load_file, make_predcition, date_extracts





# Create an instance of FastAPI
app = FastAPI(debug=True)

# get absolute path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

# set path for ml files
ml_contents_path = os.path.join(DIRPATH, '..', 'assets', 'ml_components', 'toolkit_folder')


ml_contents = load_file(ml_contents_path)

Encoder = ml_contents["OneHotEncoder"]
model = ml_contents["model"]
features_ = ml_contents['feature_names']



@app.get('/')
def root():
    return 'Welcome to the Gorecery Sales Forecasting API'

@app.get('/health')
def check_health():
    return {'status': 'ok'}

@app.post('/predict')
async def predict_sales( store_id: int, category_id: int, onpromotion: int,
                  city: str, store_type: int, cluster: int, date_: Annotated[datetime.date, "The date of sales"] = datetime.date.today()):

    input = {
    'store_id':[store_id], 
    'category_id':[category_id], 
    'onpromotion' :[onpromotion],
    'type' : [store_type], 
    'cluster': [cluster],
    'city' : [city],
    'date_': [date_]
    }   

    input_data = pd.DataFrame(input)
    date_extracts(input_data)

 
    sales = make_predcition(Encoder, model, input)
    sales_value = float(sales[0])
    return {'sales': sales_value}



if __name__ == "__main__":
    uvicorn.run('app:app', reload=True)




