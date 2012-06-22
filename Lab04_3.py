'''
Seth Fiawoo
MIT-AITI 2012
Lab04: Intro Python Data Structures
'''

#3
#a List

#b
items={'Apples':7.3,'Bananas':5.5,'Bread':1.0,'Carrots':10.0,'Champagne':20.90,'Strawberries':32.6}
items['Strawberries']=63.43
print items
items['Chicken']=6.5
print items

in_stock=[]
for i in items.items():
    in_stock.append(i[0])
    
print in_stock
print
#c
always_in_stock=tuple(in_stock)
print always_in_stock
print
#d
print 'Come to shoprite! We always sell:'
for i in range(len(always_in_stock)):
    print always_in_stock[i]

