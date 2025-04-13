from Reader import *
#---------------------------------------MOST MONEY ITEM-------------------------------------------
st.markdown("<h3 style='text-align: center;'>How much revenue does each item generate?</h3>",unsafe_allow_html=True)
MostMoneyItem = p.read_csv('Results/Transactions.csv')
MostMoneyItem.pop('quantity')
MostMoneyItem.pop('price_per_item')
MostMoneyItem = MostMoneyItem.groupby(['item']).sum('Total_Price')
MostMoneyItem = MostMoneyItem.rename(columns={'Total_Price':'Total'})
MostMoneyItem.pop('id')
st.bar_chart(data=MostMoneyItem)
#--------------------------------------------------------------------------------------------------------
