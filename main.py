import streamlit as st
import pandas as pd
import requests
import datetime

def side_bar():
    city = st.sidebar.text_input("Enter your city or country name:")
    return city

def display(weather_data):
    temp, feel = st.columns(2)
    wind, desc = st.columns(2)
    country, name = st.columns(2)
    try:
        temp.metric("Temperature", weather_data['main']['temp'], border=True)
        feel.metric("Feels like", weather_data['main']['feels_like'], border=True)

        wind.metric("Wind", weather_data['wind']['speed'] ,border=True)
        desc.metric("Description", weather_data['weather'][0]['description'] ,border=True)

        country.metric("Country", weather_data['sys']['country'], border=True)
        name.metric("Name", weather_data['name'], border=True)
    except KeyError:
        st.write("Enter correct city name!")


def next_days(weather_week):
    first_time = datetime.datetime(1970, 1, 1)
    time_list = []
    temp_list = []
    color_list = ["#88c7dc", "#FFB343", "#FF0000"]
    try:
        for values in weather_week['list']:
            seconds = values['dt']
            converted = datetime.timedelta(seconds=seconds)
            time = first_time + converted
            time_list.append(time.strftime("%Y-%m-%d %H:%M"))
            temp_list.append(values['main']['temp'])

        df = pd.DataFrame({'date': time_list, 'temp': temp_list})
        st.bar_chart(data=df, x='date', y='temp')
    except KeyError:
        st.write("Enter correct city name!")

def main():
    st.set_page_config(page_title="MyWeather")
    api_key = "79d4c5cc409902a82858318bc7da2fd9"
    city = side_bar()
    url_day = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    url_week = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url_day)
    week_response = requests.get(url_week)
    weather_data = response.json()
    weather_week = week_response.json()
    display(weather_data)
    next_days(weather_week)

main()
