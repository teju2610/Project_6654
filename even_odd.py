import streamlit as st
st.title("This is simple App")
st.header("hello world")
st.subheader("cvr")
num1=st.number_input("enter number",min_value=1,step=1)
if st.button("Even/Odd"):
   if num1%2==0:
       st.success("even number")
   else:
       st.error("odd number")
