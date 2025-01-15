import  streamlit as st

first_name = st.text_input("Enter Your First Name : ")
last_name = st.text_input("Enter Your Last Name : ")
address = st.text_input("Enter Your Address : ")
profession= st.selectbox("Enter Your Profession Details: ",("Developer","Manager","Analyst","HR"))
button = st.button("Submit")
if button :
    st.markdown(f"""
    First Name : {first_name}
    Last Name : {last_name}
    Address : {address}
    Profession : {profession}    
""")