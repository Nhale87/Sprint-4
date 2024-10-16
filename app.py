#Imported libraries
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.io as pio 
pio.templates.default = "plotly"

#Dataset
df = pd.read_csv('./datasets/vehicles_us.csv')

#
df[['model_year', 'odometer', 'is_4wd', 'cylinders']] = df[['model_year', 'odometer', 'is_4wd', 'cylinders']].fillna(0).astype('int')
df['paint_color'] = df['paint_color'].fillna('Unknown')
df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')
df[['make', 'model']] = df['model'].str.split(' ', n=1, expand=True)
known_years = df[df['model_year'] != 0]
known_years['model_year'].min()

#Header
st.header("Sprint 4 Project")

#Histogram
fig = px.histogram(known_years, x="days_listed", color='make')
fig.update_layout(yaxis_title="Count", xaxis_title='Days Listed')
st.plotly_chart(fig, use_container_width=True)


#Scatterplot and Checkbox
Vehicle_Make = st.checkbox('Fig2')
if Vehicle_Make:
    known_median = known_years.groupby(['type', 'make', 'model', 'days_listed', 'odometer'])['price'].median().reset_index()
    fig2 = px.scatter(known_median, x='make', y='price', color="type", hover_data=['model', 'days_listed', 'odometer'])
    fig2.update_layout(yaxis_title= "Price (USD)", xaxis_title= "Vehicle Make")
    st.plotly_chart(fig2, use_container_width=True)
else:
    known_median = known_years.groupby(['type', 'make', 'model', 'days_listed', 'odometer'])['price'].median().reset_index()
    fig2 = px.scatter(known_median, x='model', y='price', color="type", hover_data=['make', 'days_listed', 'odometer'])
    fig2.update_layout(yaxis_title= "Price (USD)", xaxis_title= "Vehicle Model")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("The data seems to show that the bulk of inventory will sell between two to five weeks of being listed and that the dealership puts a higher price point towards Trucks and SUVs, presumably because of demands of the demographics of the area or possibly the geographical region requires it to ease difficulty of travel.")