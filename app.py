import streamlit as st
import pickle
import numpy as np
import pandas as pd
pipe = pickle.load(open('var19.pkl','rb'))
df = pickle.load(open('var18.pkl','rb'))
st.title("Mobile Predictor")
mobile_name =df['mobile_name'].unique()
mobile_name =mobile_name.tolist()
for i, word in enumerate(mobile_name):
    mobile_name[i] = word.upper()
mobile_name = st.selectbox('Brand',mobile_name)
# type of laptop
mobile_color= df['mobile_color'].unique()
type = st.selectbox('Type',mobile_color)
ram =df['RAM'].unique()
ram = st.selectbox('RAM(in GB)',ram)
rom =df['ROM'].unique()
rom = st.selectbox('ROM(in GB)',rom)
rating =df['rating'].unique()
rating=rating.tolist()
rating[13]=0
rating = st.selectbox('RATING',rating)
df['Rear_Camera_type'] = df['Rear_Camera_type'].str.replace('MP','')
Rear_Camera_type =df['Rear_Camera_type'].unique()
Rear_Camera_type = st.selectbox('Back_Camera(in MP)',Rear_Camera_type )
df['Front_Camera'] = df['Front_Camera'].apply(lambda x:x.split()[0])
df['Front_Camera'] = df['Front_Camera'].str.replace(',','0')
df['Front_Camera'] = df['Front_Camera'].str.replace('MP','')
Front_Camera =df['Front_Camera'].unique()
Front_Camera = st.selectbox('Front_Camera(in MP)',Front_Camera)
Warranty =df['Warranty'].unique()
Warranty = st.selectbox('Warranty',Warranty)
Processor_brand =df['Processor_brand'].unique()
Processor_brand = st.selectbox('Processor_brand',Processor_brand )
df['inch'] = df['inch'].str.replace('Inch','')
df['inch'] = df['inch'].str.replace('inch','')
df['inch'] = df['inch'].fillna(0)
inch=df['inch'].unique()
inch = st.selectbox('inch(in inch)',inch )
Display_type =df['Display_type'].unique()
Display_type = st.selectbox('Display_type',Display_type )
Battery_type =df['Battery_type'].unique()
Battery_type = st.selectbox('Battery_type',Battery_type )
mobile_name =mobile_name.lower()
if st.button('Predict Price'):
   #query=pipe.predict(pd.DataFrame(columns=['rating','RAM','ROM','Warranty','mobile_name',
   # 'mobile_color','Processor_brand','inch','Display_type','Battery_type',
   # 'Rear_Camera_type','Front_Camera_type'],
   # data=np.array([rating,ram,rom,Warranty,mobile_name,mobile_color,Processor_brand,inch,
   # Display_type,Battery_type,Rear_Camera_type,Front_Camera]).reshape(1,12)))
   #query = tuple(query)
   #print(arr)
   #print(query.shape)
   #print(pipe.predict(query)[0])
   #st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))
   #st.title("The predicted price of this configuration is"+np.exp(arr))
   #print(arr)
   user_report_data = {
       'rating': rating,
       'RAM': ram,
       'ROM': rom,
       'Warranty': Warranty,
       'mobile_name': mobile_name,
       'mobile_color': mobile_color,
       'Processor_brand': Processor_brand,
       'inch': inch,
       'Display_type': Display_type,
       'Battery_type': Battery_type,
       'Rear_Camera_type': Rear_Camera_type,
       'Front_Camera_type': Front_Camera

   }
   report_data = pd.DataFrame(user_report_data)
   #report_data=report_data.reshape(1,-1)
   salary = pipe.predict(report_data)
   salary=np.array(salary)
   print(salary[0])

   #st.subheader('mobile_price_predictor')
   st.subheader("mobile_price_predict:"+' ' + str(int(np.exp(salary[0]))))