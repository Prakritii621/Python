'''
list
-list is a collection datatype that is capable of holding more than 1 variable 
-it is similar to array but has 1 fundamental difference
-it is heterogeneous for these u can put in any type of value(any datatype,yes anyyyyyyy)
-it is denoted with square brackets[]
'''
list_var=[1,2,3,4,5]
print(list_var,type(list_var))
print(list_var,list_var[4])
print('--'*10)
#loop in list:index value
for i in range(0,len(list_var)):
  print(list_var[i])
print('--'*10)
#iterating over each value itself 
for i in list_var:
  print(i)
print('--'*10)
#for finding out index and value in list:
for i,j in enumerate(list_var):
  print(i,j)
print('--'*10)
#loop over each element of the list to print only the even numbers 
list1=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,len(list1),2):
  print(list1[i])
