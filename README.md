# Name: Humberto Sanchez Rivera
# email: humberto.sanchez@upr.edu
# phone: 787-317-2845

# Introduction

    This solution processes Venmito's transaction data and presents analytical insights through interactive visualizations

# Prerequesites

Hi, to start the project your first need to have the following installed:

   -  python interpreter
   -  streamlit
   -  xml
   -  yaml
   -  pandas

With all dependencies installed, simply run from the project main directory:

# Running the Files Generators (main)

    - Run the following command in you terminal
    - python -u .\main.py

    This will read the files in data, analize them and finally generate all the csv files with the results, in folder named Results

# Illustrating the data (Reader)
After generating the CSV files, stay in the same path and run the following:

    - Run the following command in you terminal

    -  streamlit run .\Reader.py
    This will start a local streamlit server and generate all the result in the graphs and content  
    in your browser of preference.

# Page in streamlit
In that server, you will see the following pages:
    - Reader
    - Devices Per Country
    - LeastAndMostSpendDays
    - MoneySpentByID Top10
    - RevenuePerItem
    - Showing Acceptance by promotion
    - The total quantity sold for each item

#                                          WHAT EACH PAGE IS FOR

#                                                   Reader
This page displays all newly generated CSV files in table format, providing a comprehensive overview of the data in one centralized location.
#                                                   Devices Per Country
This visualization highlights the most commonly used devices across different countries.
#                                                   LeastAndMostSpendDays
This analysis identifies the highest and lowest-value transaction dates, revealing when customers spend the most and least.
#                                                   Highest_And_Lowest_Transactions_By_ID
This page displays the top 10 highest and lowest transactions, helping identify the most and least valuable orders.
#                                                   RevenuePerItem
This page shows item-level revenue, ranking products from highest to lowest earnings.
#                                                   Showing Acceptance by promotion
This page tracks how often customers accept or reject promotions, measuring campaign effectiveness.
#                                                   The total quantity sold for each item
This page visualizes sales volume per product, highlighting best-sellers and underperformers.