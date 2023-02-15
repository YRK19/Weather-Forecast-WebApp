import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout='wide')
st.title("Weather forecast for Next Days")
place = st.text_input("Place: ", placeholder="Type country name")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view", ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        data = get_data(place, days)

        if option == 'Temperature':
            dates = [i['dt_txt'] for i in data]
            temperatures = [i['main']['temp']/10 for i in data]
            figure = px.line(x=dates, y=temperatures, labels={'x': "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == 'Sky':
            dates = [i['dt_txt'] for i in data]
            sky_conditions = [i['weather'][0]['main'] for i in data]
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            image_path = [images[i] for i in sky_conditions]
            st.image(image_path, caption=dates, width=80)
        st.write("Displayed data is from https://openweathermap.org/")
    except KeyError:
        prompt = f"{place} country doesn't exist"
        st.write(prompt)
