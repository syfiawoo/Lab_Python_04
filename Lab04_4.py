'''
Seth Fiawoo
MIT-AITI 2012
Lab04: Intro Python Data Structures
Challenge Problem
'''

def binary_insert(new_float,some_list_of_floats):
    length=len(some_list_of_floats)
    mid=length/2
    lower=0
    upper=length-1
    insert=False
    if new_float<some_list_of_floats[lower]:
        some_list_of_floats.insert(lower,new_float)
        insert=True
    if new_float>some_list_of_floats[upper]:
        some_list_of_floats.insert(upper+1,new_float)
        insert=True
    #modifies the input list to include the new_float
    
    while insert==False:
        
        if new_float<some_list_of_floats[mid]:
            upper=mid
            mid=(lower+upper)/2
        if new_float>some_list_of_floats[mid]:
            lower=mid
            mid=(lower+upper)/2
        if new_float==some_list_of_floats[mid]:
            some_list_of_floats.insert(mid,new_float)
            insert=True

        if upper-lower==1:
            if new_float<some_list_of_floats[lower]:
                some_list_of_floats.insert(lower-1,new_float)
            if new_float<some_list_of_floats[upper] and new_float>some_list_of_floats[lower]:
                some_list_of_floats.insert(upper,new_float)
            if new_float>some_list_of_floats[upper]:
                some_list_of_floats.insert(upper+1,new_float)
            insert=True
        
    return some_list_of_floats

lst=[0.5,1.25,1.5,1.75,2.0,2.25]
num=1.65

new_list=binary_insert(num,lst)
print new_list


def min_cost(grocery_list,item_to_price_list_dict):
#grocery_list is a list of strings (item names)
#item_to_price_list_dict is a dictionary with key-value
# pairs as follows: the item name (strings) is the key
# and the list of prices (floats) at different grocery is
# the value
    sum_items=0.0
    for item in grocery_list:
        for i in item_to_price_list_dict.keys():
            if item==i:
                prices=item_to_price_list_dict[i]
                prices.sort()
                sum_items+=prices[0]
                 
    return sum_items

l=['Bananas','Apples','Bread']
dct={'Apples':[7.3,5.0],'Bananas':[5.5,6],'Bread':[1.0,4.0],'Carrots':[10.0,8.9],'Champagne':[20.90,22.3]}
su=min_cost(l,dct)
print su