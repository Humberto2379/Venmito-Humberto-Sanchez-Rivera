from Reader import *

#-----------------------------TRANSACTIONS
# Grouping by id, and showing all the, reseting the index in order to add x=id as a column
groupByIDTransactions = p.read_csv('Results/Transactions.csv')
groupByIDTransactions.pop('price_per_item')
groupByIDTransactions.pop('quantity')
groupByIDTransactions = groupByIDTransactions.groupby('id').sum('Total_Money_Expended')
#This markdown was just for making the text centrilize
st.markdown("<h3 style='text-align: center;'>Showing the 10 highest-spending transactions</h3>", unsafe_allow_html=True)
groupByIDTransactions = groupByIDTransactions.rename(columns={'Total_Price':'Total'})
groupByIDTransactions = groupByIDTransactions.sort_values(by='Total',ascending=False)

st.bar_chart(data=groupByIDTransactions.head(10))
#------------------------------------------------------------------------------------------------