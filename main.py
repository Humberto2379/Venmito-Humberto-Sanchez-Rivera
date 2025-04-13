import pandas as p 
import yaml as yml
import xml.etree.ElementTree as et
import streamlit
from ast import literal_eval

#------------------------------------------- READING JSON FILE PEOPLE
jsonData = p.read_json('data/people.json') # Reading the People csv file
jsonData.rename(columns={'telephone':'phone'}) # Renaming telephone to be phone column
jsonData[['city','country']] = jsonData['location'].apply(p.Series) # Making two new columns, country and city
jsonData.pop('location') # popping unused column
#----------------------------------------------------------------------------------------

#------------------------------------------- READING YML FILE PEOPLE---------------------------------------------------------------
with open('data/people.yml','r') as file: # opening the yml file
    ymlData = yml.safe_load(file) # loading the file 
       
ymlFrame = p.DataFrame(ymlData) # Converting it in a dataFrame of pandas
ymlFrame = ymlFrame.reindex(columns=['id','name','email','phone','city','Android','Desktop','Iphone'])
ymlFrame[['ciudad','country','devices','first_name','last_name']] = None


for i in range(len(ymlFrame)):
    devices = [] # Create an Empty list for devices
    location = ymlFrame.loc[i, 'city'] # It takes the city column of the current index
    citySeparator = location.find(',') # It finds the divisor, in this case is a comma
    ymlFrame.loc[i, 'ciudad'] = location[0:citySeparator] # Just the city
    ymlFrame.loc[i,'country'] = location[citySeparator+1:] # Just the country
    android = ymlFrame.loc[i,'Android'] # If it is 0 there is no Android in this user
    Desktop = ymlFrame.loc[i,'Desktop']# If it is 0 there is no Desktop in this user
    Iphone = ymlFrame.loc[i,'Iphone']# If it is 0 there is no Iphone in this user
    
    if(android == 1): # If it is 1, add an Android to the list
        devices.append('Android')
    if(Desktop == 1):# If it is 1, add an Desktop to the list
        devices.append('Desktop')
    if(Iphone == 1):# If it is 1, add an Iphone to the list
        devices.append('Iphone')
    ymlFrame.at[i,'devices'] = devices # Assign the list to the corresponding row


    name = ymlFrame.loc[i,'name']# taking the complete name
    nameDivisor = name.find(' ') # Finding the division between names and lastname
    ymlFrame.loc[i,'first_name'] = name[:nameDivisor] # saving the name in it's respective column
    ymlFrame.loc[i,'last_name'] = name[nameDivisor+1:] # saving the lastname in it's respective column


#-------------------------------- POPPING NO LONGER USEABLE COLUMNS
ymlFrame =  ymlFrame.drop(columns=['city','Android','Desktop','Iphone','name'])
ymlFrame = ymlFrame.rename(columns={'ciudad':'city'})


#------------------------------------ REINDEXING TABLES---------------------------------------------------
ymlFrame = ymlFrame.reindex(columns=['id','first_name','last_name','email','phone','city','country','devices'])
jsonData = jsonData.reindex(columns=['id','first_name','last_name','email','phone','city','country','devices'])

#------------------------------------DROPING ANY ROW THAT HAS EMPTY CELLS
ymlFrame = ymlFrame.dropna(how='any')
jsonData = jsonData.dropna(how='any')

#----------------------------------------MERGIN BOTH PEOPLE FILES--------------------------------------------------------
#CONCATING BOTH FILES, TO NOT LEAVE ANY PERSON BEHIND
merginPeople = p.concat([jsonData,ymlFrame],ignore_index=True).drop_duplicates('id')
# DROPPING DUPLICATES BY ID (it saves the first appeareance)
merginPeople = merginPeople.sort_values('id') # Order by id
merginPeople.to_csv('Results/People_Result.csv',index=False)
#------------------------------------------------------------------------------------------------

#----------------------------------READING TRANSFERS FILE---------------------------------------------
transferReader = p.read_csv('data/transfers.csv')
transferReader = transferReader.dropna(how='any') # dropping the rows that has any null values
transferReader.to_csv('Results/Transfers.csv',index=False)
#----------------------------------------------------------------------------------------------------

#----------------------------------READING TRANSACTIONS FILE---------------------------------------------
xmlData = [] # Making an empty list, for later append the data and be more easy to make a dataFrame in pandas
xmlReader = et.parse('data/transactions.xml') # The document is parsed
root = xmlReader.getroot() # Get the root of the document, in order to iterate from the begining
for tr in root.findall('transaction'):
    id = tr.attrib['id'] # getting the id, which is an attribute
    items = tr.find('items') # Save the 'container' items
    for i in items.findall('item'): # iterate into every single item inside of items
        item_name = i.find('item') # name of the item
        price = i.find('price') # price of the item
        price_per_item = i.find('price_per_item') #prices per items
        quantity = i.find('quantity') #ammount of items

        
        #appending each item individual
        xmlData.append({'id':id,
                            'item':item_name.text,
                            'Total_Price':price.text,
                            'price_per_item':price_per_item.text,
                            'quantity':quantity.text})
        
xmlDataResult = p.DataFrame(xmlData) # making the dataframe
xmlDataResult = xmlDataResult.dropna(how='any')
xmlDataResult.to_csv('Results/Transactions.csv',index=False) # turning the frame into a csv
#-----------------------------------END