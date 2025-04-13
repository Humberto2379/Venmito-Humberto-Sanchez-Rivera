from Reader import * 
from ast import literal_eval # Super important Import, without it, the frame take the list like a string
# and would be very hard to analyze the data 

st.markdown("<h3 style='text-align: center;'>Devices Uses Per Country</h3>", unsafe_allow_html=True)

merged_promotions_people = p.read_csv('Results/People_Result.csv')

merged_promotions_people['devices'] = ( # Remember the apply, works for every cell, is like doing a for loop
    merged_promotions_people['devices'] 
    .apply(lambda devices: literal_eval(devices) if isinstance(devices, str) else devices)
    # making the list an actual list instead of a str that looks like it
)
#for value counts to work in the list, we have to first make it a Series
merged_promotions_people = merged_promotions_people.explode('devices')
result = merged_promotions_people.groupby(['devices','country']).size().unstack()
st.bar_chart(result)

