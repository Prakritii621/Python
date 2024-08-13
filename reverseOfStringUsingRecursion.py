#reverse a string using recursive function
def reverse(str):
  size=len(str)
  if size==0:
    return str

  last_char=str[size-1]

  return reverse(str[0:size-1])+last_char
  reverse(str[0:size-1])
  ''' if len(str)=0
    return str
  else:
    return reverse(str[1:])'''

result=reverse("prakriti")
print(result)
