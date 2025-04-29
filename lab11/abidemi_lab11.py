"""
Abidemi Alade
Lab 11: Dictionary, Functions, Classes
April 27, 2025
"""

# import 'lab11_classes.py'
import lab11_classes

# import 'lab11_functions.py'
import lab11.abidemi_lab11 as abidemi_lab11

print("----- Example 1: Python Dictionary -----")

# create a dictionary
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# print a complete dictionary
print(car)

# access items in a dictionary we use ["KEY_NAME"]
print(f"The year of the car is: {car['year']}")

# update the value of the key
car["year"] = 1980
print(f"The year of the car was updated to: {car['year']}")

# add key:value pair
car["color"] = "red"
print(car)

print("\n----- Example 2: Loop Through Each Key in Dict. -----")
for key in car:
    print(key)

print("\n----- Example 3: Loop Through Each Value in Dict. -----")
for key in car:
    print(car[key])

print("\n----- Example 4: Loop Through Each Pair in Dict. -----")
for key in car:
    print(f"{key}: {car[key]}")

print("\n----- Example 5: Check If Key is Present in Dict. -----")
check = "owner" in car
print(f"The key 'owner' is in car?: {check}")

print("\n----- Example 6: Python Dictionary Application -----")

# given the following list, create a dict. that will count
# the number of times that a word appears in the string
# the dict. will organize the words as the keys, and the number
# of occurrence of the word as the value of the key

phrase = "to be or not to be"
phrase_split = phrase.strip().split()
phrase_map = {}

for word in phrase_split:
    if word in phrase_map:
        phrase_map[word] += 1
    else:
        phrase_map[word] = 1

print("Results of the Phrase Dictionary:")
for key in phrase_map:
    print(f"'{key}' appears {phrase_map[key]} times")

print("\n----- Example 7: Calling Functions -----")

# call function 'greeting' with no args or return
abidemi_lab11.greeting()

# call function 'print_username' with args
abidemi_lab11.print_username("Miguel")

# call function 'user_country' with default params
abidemi_lab11.user_country()
abidemi_lab11.user_country("Martha")
abidemi_lab11.user_country("Martha", "Chile")

# call function 'product' with args and returns value
num1 = 2
num2 = -6
calc1 = abidemi_lab11.product(num1, num2)
print(f"The product of {num1} and {num2} is {calc1}")

# call function 'multiple3' with args and return a boolean
checkOne = abidemi_lab11.multiple3(num1)
checkTwo = abidemi_lab11.multiple3(num2)
print(f"Is {num1} multiple of 3?: {checkOne}")
print(f"Is {num2} multiple of 3?: {checkTwo}")

# function composition
number_sum = abidemi_lab11.sum_numbers(3)
abidemi_lab11.print_results(number_sum)

print("\n----- Example 9: Built-in Functions -----")
rad = 2
area = abidemi_lab11.area_circle(rad)
abidemi_lab11.print_area(area, rad)

print("\n----- Example 10: Try/Except -----")
ratio = abidemi_lab11.hour_ratio(0)
print(ratio)

print("\n----- Example 11: Classes -----")
user1 = lab11_classes.MyClass()
print(user1)

print(f"ID of 'user1': {user1.get_id()}")

print("\n----- Example 12: Instantiating Classes -----")
# create instance of the class 'ComplexNumber'
complex_number = lab11_classes.ComplexNumber(2, 3)

# access properties of the instantiated object
real = complex_number.r
print(f"The real number of the class is: {real}")

print("\n----- Example 13: Classes (cont.) -----")
# create instance of a car
tesla = lab11_classes.Car("Tesla", "S", 2023)

# call tesla 'read_odometer' method
print(tesla.read_odometer())

# call tesla object 'get_car_description' method
print(tesla.get_car_description())

# update odometer
tesla.update_odometer(10)
tesla.read_odometer()
