# Name: Humberto Sanchez Rivera
# email: humberto.sanchez@upr.edu
# phone: 787-317-2845


# Solution Approach
My approach utilized the pandas library, which allowed me to easily read JSON, XML, and CSV files. However, for YAML files, I needed to first install yaml. After safely loading the YAML data, I converted it into a DataFrame for consistency.

The most challenging files to process were XML and YAML. The XML file required additional preprocessing. I used the ElementTree library to properly parse nested elements since pandas struggled with the indexed structure. Similarly, the YAML file needed careful handling to ensure correct formatting before conversion.

Once all the data was properly loaded and structured, I chose Streamlit for visualization. Its simplicity and efficiency made it an excellent choice for displaying the processed data.

# Prerequesites

Hi, to start the project your first need to have the following installed:

   -  python interpreter
   -  streamlit
   -  xml
   -  yaml
   -  pandas

With all dependencies installed, simply run from the project main directory:

# Running the Files Generators (main)

    - Run the following command in your terminal
    windows
        - python -u .\main.py
    linux
        - python3 -u ./main.py

    This will read the files in data, analize them and finally generate all the csv files with the results, in folder named Results

# Illustrating the data (Reader)
After generating the CSV files, stay in the same path and run the following:

    - Run the following command in your terminal
    windows
        -  streamlit run .\Reader.py
    linux
        -  streamlit run ./Reader.py
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