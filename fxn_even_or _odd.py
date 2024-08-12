'''return type function
    function that can return output to the main flow of the code '''
def even_odd_checker(x):
  if x%2==0:
    return 'even',x
  else:
    return 'odd',x
even_odd_checker(10)
'''
alt
def even_oddd_checker(x):
  if x%2==0:
    return 'even'
  else:
    return 'odd'
op=even_oddd_checker(10)
print(op)'''
