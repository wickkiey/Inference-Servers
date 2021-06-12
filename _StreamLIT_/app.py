import streamlit as st

import numpy as np
import pandas as pd


st.title('My first app')

st.write(pd.DataFrame([[1,2],[4,5]]))

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option