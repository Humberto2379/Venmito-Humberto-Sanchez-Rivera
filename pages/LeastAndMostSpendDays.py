from Reader import * 
#---------------------------MOST SPENDED IT-------------------------------------
st.markdown("<h3 style='text-align: center;'>Top 10 dates by total amount spent</h3>",unsafe_allow_html=True)
MostSpend = transferReader.rename(columns={'date':'Transaction Date'})
MostSpend = MostSpend.groupby('Transaction Date').sum('amount')
MostSpend = MostSpend.drop(columns=['sender_id','recipient_id'])
MostSpend = MostSpend.sort_values('amount',ascending=False)
st.bar_chart(MostSpend.head(10))
#---------------------------LEAST SPENDED IT-------------------------------------
LeastSpend = MostSpend.sort_values('amount',ascending=True)
st.markdown("<h3 style='text-align: center;'>Top 10 dates spend less by total amount spent</h3>",unsafe_allow_html=True)
st.bar_chart(LeastSpend.head(10))