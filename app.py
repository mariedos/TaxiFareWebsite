import streamlit as st
import numpy as numpy
import pandas as pd
import requests


'''
# TaxiFareModel front
'''

#key,pickup_datetime,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,passenger_count

key = '2015-01-27 13:08:24.0000002'
pickup_date = st.date_input('Date:')
pickup_time = st.time_input('Time:')
pickup_datetime = f"{pickup_date} {pickup_time} UTC"
pickup_longitude = st.number_input('Pickup Longitude:',value=-73.950655)
pickup_latitude = st.number_input('Pickup Latitude:',value=40.783282)
dropoff_longitude = st.number_input('Dropoff Longitude:',value=-73.984365)
dropoff_latitude = st.number_input('Dropoff Latitude:',value=40.769802)
passenger_count = st.number_input('Number of Passengers:',min_value=1, max_value=8, step=1, value=1)

input_data= {"dropoff_latitude":[dropoff_latitude],
            "dropoff_longitude":[dropoff_longitude],
            "key":[key],
            "passenger_count":[passenger_count],
            "pickup_datetime":[pickup_datetime],
            "pickup_latitude":[pickup_latitude ],
            "pickup_longitude":[pickup_longitude]}

response = requests.get("http://taxifare.lewagon.ai/predict_fare/", params = input_data)

st.markdown(f"<h1 style=‘color:#6369D1;text-align: center;’>{str(round(response.json()['prediction'],2))}</h1>", unsafe_allow_html=True)
