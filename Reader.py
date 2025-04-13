import pandas as p 
import yaml as y
import streamlit as st



peopleReader = p.read_csv('Results/People_Result.csv') # Reading People results
promotionsReader = p.read_csv('Results/Promotions.csv') # Reading Promotions results
transferReader = p.read_csv('Results/Transfers.csv') # Reading transfer results
transactionsReader = p.read_csv('Results/Transactions.csv') # Reading transactions results

st.markdown("<h1 style='text-align: center;'> DATA RESULTS</h1>",unsafe_allow_html=True) # Title
# 
st.markdown("<h3 style='text-align: center;'>PEOPLE TABLE</h3>",unsafe_allow_html=True)
st.dataframe(peopleReader)
st.markdown("<h3 style='text-align: center;'>PROMOTIONS TABLE</h3>",unsafe_allow_html=True)
st.dataframe(promotionsReader)
st.markdown("<h3 style='text-align: center;'>TRANSFERS TABLE</h3>",unsafe_allow_html=True)
st.dataframe(transferReader)
st.markdown("<h3 style='text-align: center;'>TRANSACTIONS TABLE</h3>",unsafe_allow_html=True)
st.dataframe(transactionsReader)
