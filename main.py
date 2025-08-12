import streamlit as st
import pandas as pd
import requests
import plotly as pt
import json

st.set_page_config(page_title="MyWeather")
api_key = "79d4c5cc409902a82858318bc7da2fd9"
city = st.text_input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
weather_data = response.json()

st.write(weather_data['name'] ,weather_data['main']['temp'])