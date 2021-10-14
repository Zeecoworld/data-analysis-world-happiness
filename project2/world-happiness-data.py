import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image



st.set_page_config(page_title='World Happiness Results')

st.header('WORLD HAPPINESS DATA RECORDS😻😻')

st.subheader('DATA ANALYSIS USING DATA FROM KAGGLE!!!')

## LOAD DATASETS /DATAFRAMES...

DATA = 'world-happiness-report-2021.csv'

df = pd.read_csv(DATA)

df_country = df["Country name"]



df_details = df.iloc[:, 2:]

st.dataframe(df_country)

st.dataframe(df_details)

pie_chart = px.pie(df_details[:20], title="Generosity Data of Last 20 Countries",values="Explained by: Generosity",names="Generosity")
pie_chart1 = px.pie(df_details[0:4], title="Generosity Data of First 5 Countries",values="Explained by: Generosity",names="Generosity")

st.plotly_chart(pie_chart)
st.plotly_chart(pie_chart1)





st.subheader('Finally, Which country has the highest and lowest rate of Generosity???🤔')


df_detail_by_describe = df_details.describe().loc['min':'max', "Generosity"]

st.dataframe(df_detail_by_describe)

st.subheader('Highest: Indonesia and Lowest: Greece 😢')


st.subheader(" \'GENEROSITY BREEDS HAPPINESS\' ")



