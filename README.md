# Grocery-Store-Forecasting-Challenge-For-Azubian


[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![fastapi](https://img.shields.io/badge/FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)](https://img.shields.io/badge/FastAPI-3776AB?style=for-the-badge&logo=fastapi&logoColor=white)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

<div align='center'> 
    <img src="headerimage"/>
    

</div>

## Project Description 
This project combines machine learning and FastAPI to develop a powerful and scalable application for predictive analytics and real-time data processing."


## Table of Contents
1. [Overview Of the Project](#overview)

  - [Description of dataset](#dataset)

2. [Application / Deployed Links](#application)

3. [Technology Stack](#technology)

4. [Deliverables](#deliverables)

5. [Installation](#installation)

6. [Execution](#execution)

7. [API Endpoints](#api-endpoints)

8. [App Usage](#usage)

9. [Contributing Instructions](#instructions)

10. [Collaborators](#collaborators)

10. [Contact Information](#contact)


## 1. Overview Of the Project <a name="overview"></a>



### i. Description of dataset <a name="dataset"></a>


## 2. Application / Deployed Links <a name="application"></a>

<table>
  <tr>
    <th>App</th>
    <th>Deployed links</th>
  </tr>
  <tr>
    <td>Streamlit App</td>
    <td><a href="">Sales forecasring App with streamlit</a></td>
  </tr>
  <tr>
    <td>Api</td>
    <td><a href="">Sales forecasring App with FastAPI</a></td>
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

## Execution
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