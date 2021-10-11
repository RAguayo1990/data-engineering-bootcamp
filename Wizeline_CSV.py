import pandas as pd

estProd = pd.read_csv('all_data.csv',usecols=['producto','estado'])
cadCom = pd.read_csv('all_data.csv',usecols=['cadenaComercial'])


# Number of commercial chains
print('Number of commercial chains:')
print(len(cadCom.cadenaComercial.unique()))

#Products
# Unfinished
sorted = estProd.sort_values(['estado', 'producto'], ascending=(True, True))
print(sorted.to_string())

# Commercial Chain with most products
print('Commercial chain with most products:\n')
print(cadCom['cadenaComercial'].value_counts().idxmax())



