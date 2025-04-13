from Reader import *

#-----------------------------TRANSACTIONS FILE
groupByIDTransactions = p.read_csv('Results/Transactions.csv')
#----------------------------------------------------------

#---------------------------------------------------------- THIS PART IS TO SHOW WHICH ITEMS ARE IN THE TRANSACTIONS
searcher = st.text_input('Search an ID',value=0)
try:
    searcher = int(searcher)
except:
    st.error('Must be an integer')
st.write(groupByIDTransactions[groupByIDTransactions['id'] == searcher]) # IT shows the table before the group by
groupByIDTransactions.pop('price_per_item')
groupByIDTransactions.pop('quantity')


# Grouping by id, and sum all the total
groupByIDTransactions = groupByIDTransactions.groupby('id').sum('Total_Money_Expended')
#This markdown was just for making the text centrilize

groupByIDTransactions = groupByIDTransactions.rename(columns={'Total_Price':'Total'})
groupByIDTransactions = groupByIDTransactions.sort_values(by='Total',ascending=False) # sort by total
st.markdown("<h3 style='text-align: center;'>Showing the 10 highest-spending transactions</h3>", unsafe_allow_html=True)
st.bar_chart(data=groupByIDTransactions.head(10))
st.markdown("<h3 style='text-align: center;'>Showing the 10 lowest-spending transactions</h3>", unsafe_allow_html=True)
st.bar_chart(data=groupByIDTransactions.tail(10))

#------------------------------------------------------------------------------------------------