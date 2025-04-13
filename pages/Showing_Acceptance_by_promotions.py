from Reader import * 
#-----------------------------PROMOTIONS---------------------------------------------------------
groupBYPromotions = p.read_csv('Results/Promotions.csv') # grouping by 
groupBYPromotions = groupBYPromotions.drop(columns=['client_email','telephone','id'])
Responses = (groupBYPromotions.groupby('promotion')['responded']
            .value_counts(normalize=True) # Normalize make the division around the responded totals
            .mul(100)
            .rename('percentage')
            .reset_index())
#----------------------------------ACCEPTING THE PROMOTION RATE----------------------------------------

st.markdown("<h3 style='text-align: center;'>Accept Promotion</h3>",unsafe_allow_html=True)
Responses_yes = Responses[Responses['responded'] == 'Yes']
Responses_yes = Responses_yes.groupby('promotion')['percentage'].sum()
st.bar_chart(data=Responses_yes)

#------------------------------NOT ACCEPTING THE PROMOTION RATE----------------------------------------
st.markdown("<h3 style='text-align: center;'>Not Accept Promotion</h3>",unsafe_allow_html=True)
Responses_no = Responses[Responses['responded'] == 'No']
Responses_no = Responses_no.groupby('promotion')['percentage'].sum()
st.bar_chart(data=Responses_no)