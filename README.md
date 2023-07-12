# :hourglass_flowing_sand: Grocery-Store-Forecasting-Challenge-For-Azubian

## Project Description 
This project combines machine learning and FastAPI to develop a powerful and scalable application for predictive analytics and real-time data processing."

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![fastapi](https://img.shields.io/badge/FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)](https://img.shields.io/badge/FastAPI-3776AB?style=for-the-badge&logo=fastapi&logoColor=white)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Table of Contents
1. [Overview Of the Project](#overview)

      [Description of dataset](#dataset)
      [Analysis and transforms](#analysis)

2. [Application / Deployed Links](#application)

3. [Technology Stack](#technology)

4. [Deliverables](#deliverables)

5. [Installation](#installation)

6. [Execution](#execution)

7. [API Endpoints](#api-endpoints)

8. [App Usage](#usage)

9. [Screenshots](#screenshots)

10. [Contributing Instructions](#instructions)

11. [Collaborators](#collaborators)

12. [Contact Information](#contact)






## 1. Overview Of the Project <a name="overview"></a>
This project is about building machine learning models to forecastsales on an anonymized data. The product from the model will used to build an API which will be embeded inyo our streamlit forecasting app.


### i. Description of dataset <a name="dataset"></a>


Main variable definitions

**Target**: the total sales for a product category at a particular store at a given date

**Stores_id**: the unique store id

**Category_id**: the unique Product category id

**Date**: date in numerical representation

**Onpromotion**: gives the total number of items in a Product category that were being promoted at a store at a given date

**Nbr_of_transactions**: the total number of transactions happened at a store at a given date

**year_weekofyear**: the combination of the year and the week of the year, (year_weekofyear = year*100+week_of_year

**ID**: the unique identifier for each row in the testing set: year_week_{**year_weekofyear**}_{store_id}_{Category_id}



The dataset used is the [Grocery sales](https://zindi.africa/competitions/grocery-store-forecasting-challenge-for-azubian/data),public dataset. 
This is anonymised real data. The data looks at 54 different stores in the same country and 33 different products.
The train set contains transaction information for 3 years and 6 months. You are tasked with forecasting the next 8 weeks for the same stores and same products. In this case the series is not stationary with some small seasonalities which change every year.

In order to obtain a exact copy of the dataset used in this tutorial please run the [script](https://github.com/kwasiasomani/Grocery-Store-Forecasting-Challenge-For-Azubian/tree/main/dev/datasets)  in which you will get acess to download the dataset.


###  ii. Analysis and transforms <a name="analysis"></a>

* Time series decomposition
  * Level
  * Trend
  * Seasonality 
  * Noise
  
* Stationarity
  * AC and PAC plots
  * Rolling mean and std
  * Dickey-Fuller test
  
* Making our time series stationary
  * Difference transform
  * Log scale
  * Smoothing
  * Moving average


#### :triangular_ruler: Models tested
* Randomforest [Link](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html?highlight=randomforest#sklearn.ensemble.RandomForestRegressor)
* Nearest neighbors [Link](https://scikit-learn.org/stable/modules/neighbors.html)
* XGBoost [Link](https://xgboost.readthedocs.io/en/latest/)
* DecisionTree [Link](https://scikit-learn.org/stable/modules/tree.html
* Autoregression ([AR](https://www.statsmodels.org/stable/generated/statsmodels.tsa.ar_model.AR.html))
* Seasonal autoregressive integrated moving average (SARIMA)
* Autoregressive integraded moving average (ARIMA)
  
#### Evaluation Metrics
* Root Mean Squared Error (RMSE)


<table class="table table-bordered table-hover table-condensed">
  <thead>
    <tr>
      <th title="Field #1">Model</th>
      <th title="Field #3">RMSE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Randomforest </td>
      <td align="right">64.12</td>
    </tr>
    <tr>
      <td>Decision Tree </td>
      <td align="right">55.89</td>
    <tr>
      <td>XGBOOST</td>
      <td align="right">41.41</td>
    </tr>
    <tr>
      <td>KNN</td>
      <td align="right">49.93</td>
    <tr>
      <td>AR</td>
      <td align="right">206.0</td>
    <tr>
      <td>SARIMA</td>
      <td align="right">196.49</td>
    <tr>
      <td>ARIMA</td>
      <td align="right">191.14</td>
    </tr>
  </tbody>
  </table>


  ## 2. Application / Deployed Links <a name="application"></a>

  <table>
    <tr>
      <th>App</th>
      <th>Deployed links</th>
    </tr>
    <tr>
      <td>Streamlit App</td>
      <td><a href="https://huggingface.co/spaces/KwabenaMufasa/Grocery_Store_Time_Series_Forecasting">Sales forecasring App with streamlit</a></td>
    </tr>
    <tr>
      <td>Api</td>
      <td><a href="https://bright1-sales-forecasting-ap1-2.hf.space/docs">Sales forecasring App with FastAPI</a></td>
    </tr>

  </table>

  ## 3. Technology Stack <a name="technology"></a>
  
  <table>
    <tr>
      <th>Technology</th>
      <th>Version</th>
    </tr>
    <tr>
      <td>Python</td>
      <td>3.9</td>
    </tr>
    <tr>
      <td>Sckit-learn</td>
      <td>0.24.1</td>
    </tr>
    <tr>
      <td>XGboost</td>
      <td>1.7.3</td>
    </tr>
    <tr>
      <td>FastAPI</td>
      <td>0.98.0</td>
    </tr>
    <tr>
      <td>Streamlit</td>
      <td>1.23.1</td>
    </tr>
    <tr>
      <td>Uvicorn</td>
      <td>0.22.0</td>
    </tr>
</table>

## 4. Deliverables <a name="deliverables"></a>
1. A jupyter notebook for training a classification model
2. A sales forecasting Model
3. An API App built with FastApi
4. A Streamlit app that make calls to the build and hosted API
5. A Dockerfile for easy deployment 


## 5. Installation <a name="installation"></a>
Clone the repository to your local machine:


        git clone https://github.com/kwasiasomani/Grocery-Store-Forecasting-Challenge-For-Azubian.git

Navigate to the project directory:

        cd Grocery-Store-Forecasting-Challenge-For-Azubian
Create a new virtual environment and activate the virtual:

- Windows:

        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:

        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt

## 6. Execution
1. Notebooks
To run any the notebooks:
- Navigate the project folder on anaconda terminal  `root :: Grocery-Store-Forecasting-Challenge-For-Azubian> ...`
- Run the command 'jupyter notebook'
- Navigate to the notebook '.....ipynb'
- Run cells in the notebook

2. API

To execute the API, follow these steps:
After all requirement have been install

At the root of your repository in your terminal
`root :: Grocery-Store-Forecasting-Challenge-For-Azubian> ...`
run the command:


            uvicorn src.api.api:app --reload 

OR

            python src/api/api.py

Open your browser and go to http://127.0.0.1:8000/docs to access the API documentation

3. App

To execute the app, follow these steps:
After all requirement have been install

At the root of your repository in your terminal
`root :: Grocery-Store-Forecasting-Challenge-For-Azubian> ...`
run the command:


            streamlit run src\app\app.py

Open your browser and go to http://localhost:8501




## 7. API Endpoints <a name="api-endpoints"></a>

1. **/**: This Endpoint display a welcome message-” Welcome to the Sepsis API...”.
2. **/health**: Checks status of the API
4. **/predict**: Recieve inouts and retuens a single 

## 8. App Usage <a name="usage"></a>
To test the various endpoints of the API using the provided documentation, follow these steps:

1. Start by accessing the API documentation, which provides detailed information about the available endpoints and their functionalities.

2. Locate the section that describes the input fields and parameters required for each endpoint. It will specify the expected data format, such as JSON or form data, and the necessary input fields.


4. Enter the required input data into the corresponding input fields or parameters as specified in the documentation.

5. Send the request by clicking the "Execute" button or using the appropriate method in your chosen tool. The API will process the request and generate the output based on the provided inputs.

6. Retrieve the response from the API, which will contain the generated output. This output may include predictions, probability scores, or any other relevant information related to sepsis prediction.

7. Repeat the process to test different endpoints or vary the input data to explore the capabilities of the API. Make sure to follow the documentation's guidelines for each endpoint to ensure accurate results.

Note: You can access the app and the use the same process test our app.


## 9. Screenshots

Power BI Visualization

https://github.com/kwasiasomani/Grocery-Store-Forecasting-Challenge-For-Azubian/assets/119458164/c2525faa-c05a-4326-9b3e-ae0b9632e335






## 10. Contributing Instructions <a name="instructions"></a>
To contribute to the Sentiment Analysis API, follow these guidelines:

- Fork the repository.
- Create a new branch: git checkout -b my-new-feature
- Make your changes and commit them: git commit -am 'Add some feature'
- Push to the branch: git push origin my-new-feature
- Create a new pull request


## 11. Collaborators <a name="collaborators"></a>
<table>
  <tr>
    <th>Name</th>
  </tr>
  <tr>
    <td>Bright Eshun</td>
  </tr>
  <tr>
    <td>Kwasi Asomani</td>
  </tr>
  <tr>
    <td>Stella  Oiro</td>
  </tr>
  <tr>
    <td>Linda Azdigbli</td>
  </tr>
    <tr>
    <td>Foster Kwabena Abrefa</td>
  
  </tr>
    <tr>
    <td>Joshua</td>
  </tr>
</table>

## 12. Contact Information <a name="contact"></a>

<table>
  <tr>
    <th>Name</th>
    <th>Twitter</th>
    <th>LinkedIn</th>
    <th>GitHub</th>
    <th>Hugging Face</th>
  </tr>
  <tr>
    <td>Bright Eshun</td>
    <td><a href="https://twitter.com/bright_eshun_">@bright_eshun_</a></td>
    <td><a href="https://www.linkedin.com/in/bright-eshun-9a8a51100/">@brighteshun</a></td>
    <td><a href="https://github.com/Bright136">@bright136</a></td>
    <td><a href="https://huggingface.co/bright1">@bright1</a></td>
  </tr>
  <tr>
    <td></td>
    <td><a href="https://twitter.com/EnochMaxwellson?t=AgNVmbDXDoIJOs9wcsZgLw&s=09">@enochmaxwellson</a></td>
    <td><a href="https://www.linkedin.com/in/joshua-maxwellson-316642121"></a>enochmaxwellson</td>
    <td><a href="https://github.com/Maxwellson"></a>enochmaxwellson</td>
    <td><a href="https://huggingface.co/settings/profile"></a>enochmaxwellson</td>
  </tr>

  <tr>
    <td></td>
    <td><a href=" https://twitter.com/Stella_Oiro">@Achar</a></td>
    <td><a href="https://www.linkedin.com/in/stella-achar-oiro/">@Achar</a></td>
    <td><a href="https://github.com/Stella-Achar-Oiro">@Achar</a></td>
    <td><a href="https://huggingface.co/Achar">@Achar</a></td>
  </tr>
  <tr>
    <td></td>
    <td><a href="https://twitter.com/kwabena_MuFaSa"></a>@kwabenaabrefa</td>
    <td><a href="https://www.linkedin.com/in/foster-nana-kwabena-abrefa-3b917b34/">@kwabenaabrefa</a></td>
    <td><a href="https://github.com/KwabenaMufasa"></a>@kwabenaabrefa</td>
    <td><a href="https://huggingface.co/KwabenaMufasa"></a>@kwabenaabrefa</td>
  </tr>

  <tr>
    <td></td>
    <td><a href=""></a></td>
    <td><a href=""></a></td>
    <td><a href=""></a></td>
    <td><a href=""></a></td>
  </tr>

  <tr>
    <td></td>
    <td><a href=""></a></td>
    <td><a href=""></a></td>
    <td><a href=""></a></td>
    <td><a href=""></a></td>
  </tr>
</table>

# Contributing
Do you have anything to add or fix? I'll be happy to talk about it! Open an issue/PR :) 

