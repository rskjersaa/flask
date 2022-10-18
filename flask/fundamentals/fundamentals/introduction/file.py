num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # data type 
string = 'Hello World' # data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana') # tuple
print(type(fruit)) # type check
print(pizza_toppings[1])  # output index 1 pizza topping sausage
pizza_toppings.append('Mushrooms') # adding value to toppings
print(person['name']) # dictionary access value
person['name'] = 'George' # updates if the key exists , adds a key value pair if it doesn't
person['eye_color'] = 'blue' # adding a key value
print(fruit[2])# output second index fruit banana

if num1 > 45: # conditional
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: # if the length of the string is less than 5 print it is a short word
    print("It's a short word!")
elif len(string) > 15:# if the length is longer than 15 print it is a long word
    print("It's a long word!")
else:
    print("Just right!")# else print Just Right

for x in range(5): # for loop
    print(x) # output 0,1,2,3,4
for x in range(2,5): # for loop
    print(x) #output 2,3,4
for x in range(2,10,3): # for loop range of 2-10 step 3
    print(x) #output 2, 5, 8
x = 0 # variable declaration
while(x < 5): #loop for x<5
    print(x) #output 0,1,2,3,4
    x += 1# increment by 1

pizza_toppings.pop()# remove last pizza topping
pizza_toppings.pop(1) # remove pizza topping at index 1

print(person)# prints the dictionary person
person.pop('eye_color') # removes eyecolor from the dictionary
print(person)# prints the dictionary without eye color

for topping in pizza_toppings: # loop through the pizza toppings in list
    if topping == 'Pepperoni': #If  pepperoni then print After 1st if statement
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # declare the function
    for num in range(10): # for loop to 10
        print('Hello')

print_hello_ten_times() # callin the function

def print_hello_x_times(x): # define a variable
    for num in range(x): #for loop until given number
        print('Hello')

print_hello_x_times(4) # calling the function with 4

def print_hello_x_or_ten_times(x = 10): #declaring the function
    for num in range(x): #for loop until given number default 10
        print('Hello')

print_hello_x_or_ten_times() #function call to 10
print_hello_x_or_ten_times(4) # function call to 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)

