import streamlit as st
salary=st.number_input("enter salary",min_value=1)
n=st.number_input("enter shopping bill1",min_value=1)
n1=st.number_input("enter shopping bill2",min_value=1)
n2=st.number_input("enter shopping bill 3",min_value=1)
total=n+n1+n2
percentage=(total/salary)*100
if st.button("total"):
   st.success(total)
if st.button("percentage"):
   st.success(percentage)