import pandas as pd
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

apptitle = 'Hadwin'

st.set_page_config(page_title=apptitle, layout='wide')

st.title('HADWIN progress report')
st.balloons() 

df = pd.read_excel("scores.xlsx")
# create a dropdown list to filter the subject

def plot_subject_progress(subject):
    years_quarters = df[['Year', 'Q']].astype(str).agg('Q'.join, axis=1)
    plt.figure(figsize=(10, 6))

    if pd.api.types.is_numeric_dtype(df[subject]):
     plt.plot(years_quarters, df[subject], marker='o', label=subject)
     plt.ylabel('Score')
    else:
      plt.bar(years_quarters, df[subject], label=subject)
      plt.ylabel('Grade')

    plt.title(f'{subject} Progress')
    plt.xlabel('Year-Quarter')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.show()

# List of subjects for the dropdown
subjects = ['English', 'Math', 'Science', 'Chinese', 'Basketball']

# Create an interactive dropdown menu
subject_selector = widgets.Dropdown(
    options=subjects,
    description='Subject:',
    disabled=False,
)

# Display the dropdown and plot the selected subject's progress
interact(plot_subject_progress, subject=subject_selector)

