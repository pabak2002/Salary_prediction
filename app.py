import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
from platform import python_version

model = pickle.load(open(r'C:\Users\pabak\Jupyter notebook codes\Streamlit_nba_price_prediction\abc.sav','rb'))
st.title('Player Salary ')
st.sidebar.header('Player PredictionData')
image = Image.open(r'C:\Users\pabak\Jupyter notebook codes\Streamlit_nba_price_prediction\bb.jpg')
st.image(image, '')

# FUNCTION
def user_report():
  rating = st.sidebar.slider('Rating', 50,100, 1 )
  jersey = st.sidebar.slider('Jersey', 0,100, 0 )
  team = st.sidebar.slider('Team', 0,30, 0 )
  position = st.sidebar.slider('Position', 0,10, 0 )
  country = st.sidebar.slider('Country', 0,3, 0 )
  draft_year = st.sidebar.slider('Draft Year', 2000,2020, 2000)
  draft_round = st.sidebar.slider('Draft Round', 1,10, 1)
  draft_peak = st.sidebar.slider('Draft Peak', 1,30, 1)
  version = st.sidebar.slider('Version', 1,3, 1)


  user_report_data = {
      'rating':rating,
      'jersey':jersey,
      'team':team,
      'position':position,
      'country':country,
      'draft_year':draft_year,
      'draft_round':draft_round,
      'draft_peak':draft_peak,
      'version':version
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Player Data')
st.write(user_data)

salary = model.predict(user_data)
st.subheader('Player Salary')
st.subheader('$'+str(np.round(salary[0], 2)))