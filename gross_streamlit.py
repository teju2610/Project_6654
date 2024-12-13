import streamlit as st
st.title("Gross salary")
salary=st.number_input("enter the basic salary",min_value=1)
if salary < 10000:
   HRA = (salary * 67) / 100
   DA = (salary * 73) / 100
elif salary < 20000:
   HRA = (salary * 69) / 100
   DA = (salary * 76) / 100
else:
   HRA = (salary * 73) / 100
   DA = (salary * 89) / 100
gross_salary = HRA + DA + salary
if st.button("calculate gross salary"):
   st.success(gross_salary)