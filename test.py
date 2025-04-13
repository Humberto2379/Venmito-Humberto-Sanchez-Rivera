import pandas as pd 

r = pd.read_json('data/people.json')
print(r['location'].head(5))
l = r['location'].apply(pd.Series).head(5)
print(l)
