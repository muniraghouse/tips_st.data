import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# Loading data
t_df=pd.read_csv(r"C:\Users\Administrator\Desktop\INTERN\csv datasets\tips.csv")
st.title("Tips Dataset")
def home():
    st.title("Presentation of Tips dataset")
    st.write("The Tips dataset is a data frame with 244 rows and 7 variable which represents some tipping data where one waiter recorded information about each tip he received over a period of a few months working in one restaurant.In all the waiter recorded 244 tips. The data was reported in a collection of case studies for business statistics (Bryant & Smith 1995).[4] The waiter collected several variables:The tip in dollars, the bill in dollars, the sex of the bill payer, whether there were smokers in the party,the day of the week,the time of day and the size of the party.")
def data():
    st.header('Dataframe')
    st.write(t_df)
def per():
    options=st.selectbox('**Select the predictive variables**', ["Bill",'Smoker', "Sex",'Day','Time','Size'])
    if options == 'Bill':
     p_plot()
    elif options == 'Smoker':
     a_plot()
    elif options == 'Sex':
     s_plot()
    elif options == 'Day':
     d_plot()
    elif options == 'Time':
     l_plot()
    elif options == 'Size':
     sz_plot()

def rep():
    st.header("REPORT")
    st.write("In conclusion, the analysis of the tips dataset revealed several interesting patterns and trends. It was found that tips were higher on weekends, and higher for larger parties.Additionally, there was a positive correlation between the total bill and the tip amount.The male persons giving more tips compare to the females.However, it should be noted that the dataset was limited to a single restaurant and may not be generalization to all restaurants.")
    st.write("Future research could expand the sample to include tips from multiple restaurants to better understand the general trends in tipping behavior.")

def p_plot():
    st.header("Total Bill vs Tip")
    fig = px.scatter(t_df, y='tip', x='total_bill')
    st.plotly_chart(fig, use_container_width=True)

def a_plot():
    st.header("Smoker vs Tip")
    fig1 = px.box(t_df, y='tip', x='smoker')
    st.plotly_chart(fig1, use_container_width=True) 

def s_plot():
    st.header("Gender vs Tip")
    fig2 = px.box(t_df, x="sex", y="tip")
    st.plotly_chart(fig2, use_container_width=True) 

def d_plot():
    st.header("Day vs Tip")
    fig2 = px.box(t_df, x="day", y="tip")
    st.plotly_chart(fig2, use_container_width=True) 

def l_plot():
    st.header("Time vs Tip")
    fig2 = px.box(t_df, x="time", y="tip")
    st.plotly_chart(fig2, use_container_width=True) 

def sz_plot():
    st.header("Size vs Tip")
    fig2 = px.box(t_df, x="size", y="tip")
    st.plotly_chart(fig2, use_container_width=True) 


st.sidebar.title('Navigation')
side = st.sidebar.radio('Select what you want to display:', ['Home', 'DataFrame', 'Tips Info', 'Report'])
if side == 'Home':
 home()
elif side == 'DataFrame':
 data()
elif side == 'Tips Info':
 per()
elif side == 'Report':
 rep()
