import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
import pickle
import datetime
import sklearn

app = Flask(__name__,template_folder="templates")

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

def encoding(meal,room,market):
    
    meal_mapping = {
    'Meal Plan 1': 0,
    'Meal Plan 2': 1,
    'Meal Plan 3': 2,
    'Not Selected': 3
    }

    room_mapping = {
    'Room_Type 1': 0,
    'Room_Type 2': 1,
    'Room_Type 3': 2,
    'Room_Type 4': 3,
    'Room_Type 5': 4,
    'Room_Type 6': 5,
    'Room_Type 7': 6,
    }

    market_mapping = {
    'Online': 0,
    'Offline': 1,
    'Corporate': 2,
    'Aviation': 3,
    'Complementary':4
    }
    meal = meal.map(meal_mapping)
    room = room.map(room_mapping)
    market = market.map(market_mapping)
    return meal,room,market


def date(date_of_reservation):
    date_of_reservation= pd.to_datetime(date_of_reservation)
    month = date_of_reservation.dt.month
    year = date_of_reservation.dt.year
    return month,year

def scaler_processing(data):
    data= scaler.transform(data)
    return data 
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
   
    input_data = pd.DataFrame([data])
  
    input_data['number of adults'] = input_data['number of adults'].astype(int)
    input_data['number of children'] = input_data['number of children'].astype(int)
    input_data['number of weekend nights'] = input_data['number of weekend nights'].astype(int)
    input_data['number of week nights'] = input_data['number of week nights'].astype(int)
    input_data['car parking space'] = input_data['car parking space'].astype(int)
    input_data['lead time'] = input_data['lead time'].astype(int)
    input_data['repeated'] = input_data['repeated'].astype(int)
    input_data['P-C'] = input_data['P-C'].astype(int)
    input_data['P-not-C'] = input_data['P-not-C'].astype(int)
    input_data['average price'] = input_data['average price'].astype(float)
    input_data['special requests'] = input_data['special requests'].astype(int)
    
    input_data['type of meal'], input_data['room type'], input_data['market segment type'] = encoding(
        input_data['type of meal'],
        input_data['room type'],
        input_data['market segment type']
    )
    
    input_data['month'], input_data['year'] = date(input_data['date of reservation'])
    
    input_data.drop('date of reservation', axis=1, inplace=True)
    
    input_data = input_data[[
        'number of adults', 'number of children', 
        'number of weekend nights', 'number of week nights', 
        'type of meal', 'car parking space', 
        'room type', 'lead time', 
        'market segment type', 'repeated', 
        'P-C', 'P-not-C', 
        'average price', 'special requests', 
        'month', 'year'
    ]]
    
    
    input_data = scaler_processing(input_data)
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
            result = "Not Canceled"
    else:
            result = "Canceled"
       
    return render_template('index.html', prediction_text='Prediction: {}'.format(result))
        
    


if __name__ == '__main__':
    app.run(debug=True)
