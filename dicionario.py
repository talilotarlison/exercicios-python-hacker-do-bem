#dicionarios

dict = {'Age' : 34, 'City' : 'Rome', 'Year' : 2016, 'Month' : 'March' }
print ("dict['City']: ", dict['City'])
# dict['City']: Rome
print ("dict['Year']: ", dict['Year'])
# dict['Year']: 2016

#modificando dados

dict['Year'] = 2015
print ("dict['Year']: ", dict['Year'])
# dict['Year']: 2015


# Adicionar um novo elemento e exibir o número de elementos em um exemplo de dicionário

dict['Sport'] = "Swimming"
len(dict)
# 5