import streamlit as st
project=st.number_input("enter the project score",min_value=1)
internal=st.number_input("enter the internal score",min_value=1)
external=st.number_input("enter the external score",min_value=1)
if st.button("Calculate"):
   if project>=50 and internal>=50 and external>=50:
       pro=(project*70/100)
       inter=(internal*10/100)
       exter=(external*20/100)
       total=pro+inter+exter
       if total>=90:
           st.success(f"A grade total marks{total}")
       elif total>80:
           st.success(f"B grade total marks{total}")
       else:
           st.success(f"C grade total marks{total}")
   else:
       if(internal<50):
           st.error(f"failed in internal {internal}")
       if(external<50):
           st.error(f"failed in external {external}")
       if project<50:
           st.error(f"failed in project {project}")