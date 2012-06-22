'''
Seth Fiawoo
MIT-AITI 2012
Lab04: Intro Python Data Structures
'''
#1
groceries=['bananas','strawberries','apples','bread']
#a
groceries.append('champagne')
print groceries
#b
groceries.remove('bread')
print groceries
#c
groceries.sort()
for item in groceries:
    print 'Go to Aisle '+item[0]+' for '+item
    

