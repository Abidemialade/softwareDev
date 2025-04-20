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