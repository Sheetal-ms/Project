import streamlit as st
import pandas as pd 
import plotly.express as px
import gzip, pickle
import matplotlib.pyplot as plt
import seaborn as sns




model=pickle.load(open('model.p','rb'))





Real_data = pd.read_csv("Delhi.csv",index_col=[0],parse_dates=[0],skiprows=2)
Real_data['pm25']=pd.to_numeric(Real_data['pm25'],errors='coerce')
Eda_data = pd.read_csv("Delhi_EDA.csv",index_col=[0],)



html_temp = """

"""

nav =st.sidebar.write('Data Pages')



nav = st.sidebar.selectbox("select",['Home',"Before EDA","After EDA","Prediction"])




if nav == "Home":
	st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1697adb8-bfb5-49b1-85c1-efde49d71052/dcxuq07-97996a2d-1833-4256-bbf5-4b979098765b.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE2OTdhZGI4LWJmYjUtNDliMS04NWMxLWVmZGU0OWQ3MTA1MlwvZGN4dXEwNy05Nzk5NmEyZC0xODMzLTQyNTYtYmJmNS00Yjk3OTA5ODc2NWIuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.-EFscCgfd20S5YLV7vTF00MzWmP-IsRkEJ2ARYVcx-w")
    }
   .sidebar .sidebar-content {
        background: url("https://www.blogenium.com/wp-content/uploads/2019/08/blogenium-dark-wallpapers-backgrounds-3.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

	html_temp = """
<h1 style="color:green;text-align:center;">Airqulity(PM2.5) Prediction </h>
<h2 style="color:green">Group 3</h2>
 <img src="https://www.aqi.in/share/1549646231DelhiAQI(AirQualityIndex),AirPollution.jpg" alt="Girl in a jacket" width="800"> 
</div>

"""



st.markdown(html_temp,unsafe_allow_html=True)

    

if nav == "Before EDA":
    col1, col2 = st.beta_columns([1,1])
    with col1:
    	if st.sidebar.checkbox("Show Data"):
        	st.dataframe(Real_data, width = 600 , height = 200 )
    with col2:
    	if st.sidebar.checkbox("Summarry"):
    		st.write(Real_data.describe())
    
    graph = st.sidebar.radio("Graph",["None","Histogram","Line Plot"])
    if graph=="None":
       st.write('')
    if graph == "Histogram":
       st.write(sns.distplot(Real_data))
       st.set_option('deprecation.showPyplotGlobalUse', False)
       st.pyplot()
    if graph == "Line Plot":
       
        
        fig = px.line(Real_data, title = 'PM2.5 Value On Monthly With Slider', width = 800)

        fig.update_xaxes(
            rangeslider_visible = True)
        st.plotly_chart(fig)
       
    
       
if nav == "After EDA":
    col1, col2 = st.beta_columns([1,1])
    with col1:
    
    	if st.sidebar.checkbox("Show Data"):
        	st.dataframe(Eda_data, width = 600 , height = 200 )
    with col2:
    	if st.sidebar.checkbox("Summarry"):
    		st.write(Eda_data.describe())
    
    graph = st.sidebar.selectbox("",["Histogram","Line Plot"])

    if graph == "Histogram":
       st.write(sns.distplot(Eda_data))
       st.set_option('deprecation.showPyplotGlobalUse', False)
       st.pyplot()
    if graph == "Line Plot":
       
        
        fig = px.line(Eda_data , y = 'pm25', title = 'PM2.5 Value On Monthly basis', width = 800)

        fig.update_xaxes(
            rangeslider_visible = True)
            
        st.plotly_chart(fig)

if nav == "Prediction":
    st.header("Forcasting Value")
    val = st.number_input('Enter the Number', min_value = 1, max_value = 24)
    index_future_dates=pd.date_range(start='2018-04-20 01:00:00',periods=val,freq='H')
    st.write(val,"Hours Of Prediction")
    pred=model.predict(start=len(Real_data),end=len(Real_data)+val-1,typ='levels').rename('ARIMA Predictions')
    pred.index=index_future_dates
    if st.button("Predict"):
    	st.write((pred), width = 600 , height = 500 )
    if st.sidebar.checkbox('Predicted graph'):
    	fig = px.line(pred, title = 'Predicted PM2.5', width = 800)
    	
    	fig.update_xaxes(rangeslider_visible = True)
    	st.plotly_chart(fig)
