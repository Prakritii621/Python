'''
libraries/packages

-collection of codes and resources that has a lot of functions and operations already written for us 

-readymade code 

-examples of libraries are tenserflow,Pytorch, Keras, Numpy......

-not all packages are directly installed with python. those libraries that cme installed with python are called preinstalled libraries. Others are to be installed manually.
-security issues pani kahile kahi arise huna sakcha 

'''
#pandas and numpy
'''installing packages 
    pip install(package_name)'''

import pandas as pd #pandas ko shortcut:pd numpy:np
'''
# Pandas Library:
# - Pandas is used for data manipulation and analysis in Python, similar to SQL.
# - It works with table-like data structures (DataFrames).
# - Pandas is best for in-memory data operations, while SQL is better for large-scale database management.
'''
# Sample dictionary to convert into DataFrame
dictionary_variable = {
    'student': ['ram', 'sam', 'hari'],
    'marks': ['20', '30', '40']  # Corrected the list with properly separated values
}

# Create a DataFrame from the dictionary
data_frame_variable = pd.DataFrame(dictionary_variable)  # Converts dictionary to DataFrame (table-like structure)
print('before adding new column ')
print(data_frame_variable)
data_frame_variable['social_Skills']=['10','20','30']
print('after adding new column')
print(data_frame_variable)

#removing column
data_frame_variable=data_frame_variable.drop(columns=['social_Skills'])
print(data_frame_variable)
#random comment 

