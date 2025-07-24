# Weather Wizard App

# from pyngrok import ngrok

# ngrok.set_auth_token("2NKWodIPjr7VXlR3xcliyJbLj1i_44SgEKPavA6KMd97TpcTS")

import streamlit as st
import requests

# Set the title of the app
st.title('🌡️ Weather Wizard 🧙‍♂️')

# Get the user's location
location = st.text_input('Enter your location:')

# Get the user's preferred units of measurement
units = st.selectbox('Choose your preferred units:', ('metric', 'imperial'))

# Set the API endpoint and parameters
api_key = '526686faae63d311cd78f142f178b94f'
endpoint = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={units}'

# Make the API request and get the response data
response = requests.get(endpoint)
data = response.json()

# Check if the location is valid
if data['cod'] == 200:
    # Display the current weather data
    st.write(f'Current temperature: {data["main"]["temp"]}')
    st.write(f'Humidity: {data["main"]["humidity"]}')
    st.write(f'Wind speed: {data["wind"]["speed"]}')

    # Set the forecast endpoint and parameters
    forecast_endpoint = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units={units}'

    # Make the forecast API request and get the response data
    forecast_response = requests.get(forecast_endpoint)
    forecast_data = forecast_response.json()

    # Display the 7-day forecast
    st.write('7-day forecast:')
    for day in forecast_data['list']:
        st.write(f'Date: {day["dt_txt"]}')
        st.write(f'Temperature: {day["main"]["temp"]}')
        st.write(f'Weather: {day["weather"][0]["description"]}')
else:
    # Display an error message if the location is invalid
    st.write('Invalid location. Please try again.')

# from pyngrok import ngrok

# public_url = ngrok.connect(port='80')
# print(public_url)