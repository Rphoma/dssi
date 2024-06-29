import pandas as pd
import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns


apptitle = 'DSSI Toy App'

st.set_page_config(page_title=apptitle, layout='wide')

st.title('My First Streamlit Application')
st.write('Reference: https://docs.streamlit.io/en/stable/api.html#display-data')
st.balloons() 

df = pd.read_excel("G:/My Drive/油池小学/Hadwin/scores.xlsx")
df['Date_combined'] = df['Year'].astype("str") + "_" + df['Q'].astype("str")
fig, ax = plt.subplots(figsize=(6, 3))
df.plot(x='Date_combined', y='English', ax=ax, kind='bar')
st.pyplot(fig)
st.dataframe(df, use_container_width=True)

