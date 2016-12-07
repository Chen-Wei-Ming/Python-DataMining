import pandas as pd

data = pd.read_csv('Data/dataset-utf8.csv')

dataContent = data['postContent']

char = '元'
print(char.encode('big5'))

# for item in dataContent :
#     print(item.encode('utf-8').decode('big5'))
