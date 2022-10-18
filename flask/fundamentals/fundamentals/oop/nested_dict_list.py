# print('hello world')

from curses import keyname
from unicodedata import name


# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # update list
# # (x[1][0]) = 15
# # print(x)
# # Change the last name of first student from jordan to bryant

# students[0] ["last_name"] = "Bryant"
# print(students)

# # In the sports directory, change "messi" to 'Andres'
# sports_directory ['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# # Change the value of 20 in Z to 30
# z[0]['y'] = 30
# print(z)

# iterate through a list of dictionaries
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(list):
#     for i in range(0,len(list)):
#         output = ""
#         for key,val in list[i].items():
#             output += f" {key} - {val},"
#         print(output)
# iterateDictionary(students)





# def iterateDictionary2(key_name, list):
#     for i in range(0,len(list)):
#         for key,val in list[i].items():
#                 if key == key_name:
#                     print(val)
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
ß


# Create a function printInfo
# def printInfo(dict):
#     for key,val in dict.items():
#         print (f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#                 print(val[i])

# printInfo(dojo)

import datetime

time_now = datetime.datetime.now().strftime("%H:%M:%S")

print(time_now)