#Global and Local variable
#function bhitra banako variable lai bahira kasaile chindaina 
global_var=10
def local_function():
  local_variable=10 #scope of this variabl eis only within this function 
  print(f'Global Variable:{global_var}')#since it global variabl eit gets printed as well
  print (local_variable)#but it gets printed here
local_function()
# print (local variable) : yeso garda local_cariable lai kasaile pani chindaina cause its scope is limited only within the function 
