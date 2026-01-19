import streamlit as st

st.title('CALCULATE BMI')

wt = st.number_input('ENter your weight in Kgs:')
h = st.number_input('ENter your height in M:')
if h==0:
    bmi=0
else:
    bmi = wt/h**2
    
st.success(f'Your BMI is(bmi)kg/M^2')