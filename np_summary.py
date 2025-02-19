import pandas as pd

totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index('name')

print(totals.head())
print("h")
print(counts.head())
month = totals.sum(axis = 1)/ counts.sum(axis =1)

print(month)


city = totals.sum(axis = 0)/counts.sum(axis = 0)
print(city)



if salary > 500000:
    data['category'] = "High"
else
      data['category'] = "Low"

data['Department'].sort()
data["Salary"].sort(acesending = false)
 
