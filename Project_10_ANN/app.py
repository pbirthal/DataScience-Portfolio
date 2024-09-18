import streamlit as st 
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle 
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder
import os
#model = load_model('model.h5')
# Ensure the model file is included in the GitHub repository
model_path = 'model.h5'
if os.path.exists(model_path):
    model = load_model(model_path)
else:
    st.error("Model file not found. Please ensure 'model.h5' is in the repository.")
##load the encoder and scaler 
with open('label_encode.pkl', 'rb') as file : 
    label_encode = pickle.load(file)

with open('onehot.pkl', 'rb') as file : 
    onehot = pickle.load(file)
    
with open('scaler.pkl', 'rb') as file : 
    scaler = pickle.load(file)
    
## Streamlit app
st.title('Customer Churn Prediction')

geography = st.selectbox('Geography', onehot.categories_[0])
gender = st.selectbox('Gender', label_encode.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

# User input for the model
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encode.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

geo_encoded = onehot.transform([[geography]])
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot.get_feature_names_out())
input_data = pd.concat([input_data.reset_index(drop=True),geo_encoded_df], axis = 1)

input_data_scaled = scaler.transform(input_data)

# Predict the customer churn
prediction = model.predict(input_data_scaled)
prediction_prob= prediction[0][0]

if prediction_prob > 0.5:
    st.write('The customer is likely to churn with a probability of {:.2f}%'.format(prediction_prob*100))
else: 
    st.write('The customer is likely to stay with a probability of {:.2f}%'.format((1-prediction_prob)*100))
    