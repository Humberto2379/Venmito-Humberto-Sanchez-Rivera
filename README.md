Name: Humberto Sanchez Rivera
email: humberto.sanchez@upr.edu
phone: 787-317-2845

# Introduction

    This solution processes Venmito's transaction data and presents analytical insights through interactive visualizations

# Prerequesites

Hi, to start the project your first need to have install:

   -  python interpreter
   -  streamlit
   -  xml
   -  yaml
   -  pandas

With all dependencies installed, simply run from the venmito-main directory:

# Running the Files Generators (main)

    - python -u .\main.py

    This will generate all the csv files with the results

# Illustrating the data (Reader)
After generating the CSV files, stay in the same path and run the following:
    
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
This visualization highlights the most commonly used devices across different countries, enabling targeted resource allocation.
#                                                   LeastAndMostSpendDays
This analysis identifies the highest and lowest-value transaction dates, revealing when customers spend the most and least. By visualizing these trends, Venmito can strategically time promotions—boosting sales during slower periods.
#                                                   MoneySpentBYID Top 10

#                                                   RevenuePerItem

#                                                   Showing Acceptance by promotion

#                                                   The total quantity sold for each item
