'''#dictionary
#it is a collection data base with key and value pair
# it works on similar concept as hash mapping 
#key holds the address of the element and value holds the element
classic dictinary can be the eg
word:meaning 
it s denoted by {} bracket 
keys can even hold lists and dictionaries
eg: dictionary_val={'key1'=[10,20,30,40]}
key is always a string
value can be anything
'''
dictionary_val={
    'key1':'10',
    'key2':'20',
    'key3':'30'
}
print(dictionary_val['key1'])
print(dictionary_val.keys(),dictionary_val.values())
print('--'*10)
#approaches for dictionary
#1: using a list
#one to one mapping of elements 
list_keys=['apple','ball','cat']
value_list=['red fruit','toy','meow machine']
#dict() keywor converts into dictionary
dictionary_val2=dict(zip(list_keys,value_list))#zip merges the values number of keys nad values need to be same 
print(dictionary_val2)
