import streamlit as st
from agent import process_query

st.title("AI Smart Assistant")

query = st.text_input("Ask something (example: weather in Hyderabad)")

if st.button("Get Weather"): #means submit button
    result = process_query(query)
    st.write(result)

