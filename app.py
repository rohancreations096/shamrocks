import streamlit as st
import joblib
st.title('loan approval process automation')
model = joblib.load('D:/java/loan_data1.joblib')
gender=st.number_input('enter gender ')
married=st.number_input('enter martial status ')
income=st.number_input('enter income ')
la=st.number_input('enter loan amount')
if st.button('predict approval'):
    prediction=model.predict([[gender,married,income,la]])
    if prediction == 'Y':
        st.text('loan approved')
    else:
        st.text('loan rejected')
