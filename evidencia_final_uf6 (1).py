# -*- coding: utf-8 -*-
"""Evidencia Final UF6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XSJDqknf0-jfU2vY3MCwc0u3tdGSnIEe
"""

import streamlit as st
import pandas as pd

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df=pd.read_csv('https://drive.google.com/file/d/1sUXMxryvguQp81yseLxYymTX5RxaH0e9/view?usp=drive_link/Police_Department_Incident_Reports__2018_to_Present.csv')

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa=pd.DataFrame()
mapa=mapa.dropna()
st.map(mapa.astype(int))