import pandas as pd 

print("Extract Data")
data = {
    'ID':[101, 102, 103],
    'Name': ['Saurabh', 'Amar', 'Amit'],
    'Age': [29, 32, 26]
}
df = pd.DataFrame(data)
print(df)