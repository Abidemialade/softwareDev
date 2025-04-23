'''
Abidemi Alade
4/20/2025
'''
#Single line comment

print("Good morning, This is my python code")
print("\n--- Example 1: string characters ------")
print("\tGood morning! \nThis is my \"python\" code")
print("\n--- Example 2: data type ------")
print(f"Data type of 3.56 = {type(3.56)}")
print(f"Data type of -25 = {type(-25)}")
print(f"Data type of 'Hello world!' = {type('Hello world!')}")
print(f"Data type of True = {type(True)}")
print(f"Data type of character '$' = type('$')")

print("\n--- Example 3: Variables ------")
#declate variables
name = "Abidemi Alade"
number1 = 3.56
number2 = -25
add_number = number1 + number2
is_raining = True
#prompt results
print(f"Name = {name}, the sum of {number1} and {number2} = {add_number}")
print(f"Is it raining? = {is_raining}")

print("\n--- Example 4: Assigning values to multiple variables -------")
#declare multiple variables 
item1, item2, item3 = "apple", 25, False
print(f"item1 = {item1}, item2 = {item2}, item3 = {item3}")
#declare multiple variables with same value
score1 = score2 = score3 = 100
print(f"score1 = {score1}, score2 = {score2}, score3 = {score3}")

print("\n--- Example 5: input command -------")
print("Enter your name: ")
username = input()
print(f"Collected username = {username}")

luckynumber = input("Enter your lucky number: ")
print(f"Lucky number = {luckynumber}")

#double lucky number
dblucky = luckynumber * 2
print(f"Double lucky number = {dblucky}")

triplenumber = str(dblucky) * 3
print(f"Triple lucky number = {triplenumber}")


#cast integer to bool value
# 0 = False, any other number = True
completed_task = -20
print(f"completed_task = {bool(completed_task)}")

print("\n--- Example 6: arithmetic operators -------")

num1 =5
num2 =9

print(f"The sum of {num1} and {num2} = {num1 + num2}")
print(f"The difference of {num1} and {num2} = {num1 - num2}")
print(f"The product of {num1} and {num2} = {num1 * num2}")
print(f"The quotient of {num1} and {num2} = {num1 / num2}")
print(f"The remainder of {num1} and {num2} = {num1 % num2}")
print(f"The exponent of {num1} and {num2} = {num1 ** num2}")
print(f"The floor division of {num1} and {num2} = {num1 // num2}")

print("\n--- Example 7: finding the hypothesis -------")
#declare and assign values

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
#calculate the hypothesis
hyp = (x**2 + y**2)**0.5
#prompt result
print(f"The hypothesis of the triangle with sides {x:0.1f} and {y:0.1f} = {hyp:5.2f}")


print("\n--- Example 8: assignment operators -------")
n = 2
print(f"number = {n}")
n += 3
print(f"number + 3 = {n}")
n -= 4
print(f"number - 4 = {n}")
n *= 5
print(f"number * 5 = {n}")
n /= 2
print(f"number / 2 = {n}")
n %= 3
print(f"number % 3 = {n}")
n **= 2
print(f"number ** 2 = {n}")
n //= 3
print(f"number // 3 = {n}")


print("\n--- Example 9: comparison operators -------")
n1 = 5
n2 = 10
n3 = 7
compare1 = n1 == n2
compare2 = n1 == n2+n3
print(f"n1 == n2 = {compare1}")
print(f"n1 == n2 + n3 = {compare2}")
compare3 = n1 > n2
compare4 = n2 <= n3
print(f"n1 > n2 = {compare3}")
print(f"n2 <= n3 = {compare4}")


print("\n--- Example 10: string indexing -------")
username = "peterpan123"
#positive indexing
print(f"The fifthenth character of {username} = {username[4]}")

#negative indexing
print(f"The last character of {username} = {username[-1]}")

print("\n--- Example 11: string slice -------")
#slice from the beginning to the 4th character
print(f"The first four characters of {username} = {username[:4]}")
#slice from the 5th character to the end
print(f"The characters from the 5th to the end of {username} = {username[4:]}")
#slice from the 3rd to the 8th character
print(f"The characters from the 3rd to the 8th of {username} = {username[2:8]}")

#slice from 4th to the 6th character using negative indexing
print(f"The characters from the 4th to the 8th of {username} = {username[-8:-5]}")

print("\n--- Example 12: Total characters in a string (len) -------")
print(f"The username has = {len(username)} characters")


print("\n--- Example 13: strip() method -------")
username = "  peterPAN123  "
print(f"The username = {username}. End of username")
username = username.strip()
print(f"The username after method strip = {username}. End of username")

print("\n--- Example 14: upper and lower method -------")
username = username.lower()
print(f"The username after method lower = {username}. End of username")
username = username.upper()
print(f"The username after method upper = {username}. End of username")

print("\n--- Example 15: replace method -------")
username = username.replace("P", "%")
print(f"The username after method replace = {username}. End of username")

print("\n--- Example 16: split method -------")
msg = "Introduction to python programming! Today we are learning string methods"
print(f"The message =       {msg}")
print(f"The message after method split = {msg.split('!')}")


print("\n--- Example 17: find method -------")
# find the letter 'P'
index_P = msg.find("P")
print(f"The index of the letter 'P' in the message = {index_P}")
# find the second letter 'P'
sec_index_P = msg.find("P", index_P + 1)
print(f"The index of the second letter 'P' in the message = {sec_index_P}")
#find a non-existing letter 'Y'
index_Y = msg.find("Y")
print(f"The index of the letter 'Y' is = {index_Y}")

print("\n--- Example 18: in, not in statement -------")
# check if the letter 'we' is in the message string
answer_we = "we" in msg
print(f"Is the letter 'we' in the message? = {answer_we}")

print ('\n ------ Example 19: list indexing ------')
colors = ['orange', 'red', 'olive']
numbers = [6, 20, -9, 5, -12]
mixedlist = [False, 20, 'peter', True, -9]
emptylist = []
print (f"colors list = {colors}")
print (f"numbers list = {numbers}")
print (f"emptylist list = {emptylist}")
print (f"mixedlist = {mixedlist}")

print (f" 2nd colors = {colors[1]}")
print (f" 1nd number = {numbers[0]}")
# print (f"3rd value = {emptylist[2]}") # can't return empty character

print (f"last color = {colors[-1]}")
print (f"3rd last number = {numbers[-3]}")



print ('\n ------ Example 20: + * operator on list ------')
new_color = colors[0] + colors[-1]
print (f"the new colore is = {new_color}")

new_word = colors[1] + numbers[2]
print (f"the new word is = {new_word}")   # data type error 



print ('\n ------ Example 21: remove item from list ------')
#remove the last color
colors.pop(-2)
print (f"colors after pop = {colors}")


print ('\n ------ Example 22: adding item to the list ------')
# add items to the end of the list colors
colors.append('pink')
print (f"colors list after append = {colors}")

# add a new list to a list
colors.append(['blue', 'green'])
print (f"colors list after append = {colors}")

# add multiple items to a list
colors.append('red', 'black') 
print (f"colors list after append = {colors}") # argument error



print ('\n ------ Example 23: sort method ------')
colors = ['orange', 'red', 'Olive']
print (f"colors list = {colors}")
colors.sort()
print (f"color list sorted = {colors}")

bool_list = [True, True, False]
bool_list.sort()
print (f"bool list sorted = {bool_list}")


print ('\n ------ Example 24: count method ------')
count_true = bool_list.count(True)
print (f"there is {count_true} True values")

count_black = colors.count('black')
print (f"there is {count_black} black colors")



print ('\n ------ Example 25: lenght of the list ------')
lenght_colors = len(colors)
print (f"there is {lenght_colors} colors")



print ('\n ------ Example 26: lenght of the index ------')
index_red = colors.index('red')
print(f"the index color red is {index_red}")

#index_green = colors.index('green')
#print(f"the index color green is {index_green}") # error

