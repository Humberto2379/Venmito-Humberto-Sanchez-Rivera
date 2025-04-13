from Reader import *

#-----------------------------BEST SELLER ITEM-----------------------------
st.markdown("<h3 style='text-align: center;'>The total quantity sold for each item</h3>",unsafe_allow_html=True)
BestSellerItem = p.read_csv('Results/Transactions.csv')
BestSellerItem.pop('Total_Price')
BestSellerItem.pop('price_per_item')
BestSellerItem = BestSellerItem.groupby(['item']).sum('quantity')
# Here I show the item that most sell, not necessary the one that make the most money
BestSellerItem.pop('id')
st.bar_chart(data=BestSellerItem)
#---------------------------------------------------------------------------------