'''
Abidemi Alade
April 25, loops
'''

print("------ Example 1: for As A Counter -----")
for i in range(0, 4):
  print(f"Hello, #{i}")

print("\n------ Example 2: for loop in a list -----")
fruits = ['apples', 'oranges', 'grapes', 'kiwis', 'pineapple']
for fruit in fruits:
  print(fruit)

print('\n')

for i in range(0, len(fruits)):
  print(f"Fruits: {fruits[i]}, Index: {i}")

print("\n------ Example 3: for loop with increment -----")
for num in range(2,30, 3):
  print(num)

print("\n------ Example 4: for loop decrement -----")
for num in range(10, 0, -2):
  print(num)

print("\n------ Example 5: for loop string -----")
str = 'PeterPan123'
for char in str:
    print(char)

print("\n------ Example 5: for loop with nested conditional statement -----")
numbers = [5, -2, 0, 8, 9, -1]
negatives = 0
for num in numbers:
  if (num < 0):
    negatives+=1
print(f"{negatives} in numbers list")

print("\n------ Example 6: for loop with nested conditional statement and operations -----")
odd_sum = 0
for num in numbers:
  if not(num % 2 == 0):
    odd_sum+=num
print(f"The sum of all odd numbers is: {odd_sum}")

print("\n------ Example 7: for loop and terminate loop when it reaches 5 -----")
for n in range(10):
  if n == 5:
    print('terminated')
    break
  print(n)

print("\n------ Example 10: else statement in a for loop -----")
for n in range(6):
  if n == 3:
    break
  print(n)
else:
  print('Loop completed')

print("\n------ Example 11: while loop as counter -----")
i = 0
while i < 6:
  print(i)
  i+=1

print("\n------ Example 12: while loop as counter -----")
sum_of_inputs = 0

while True:
  number = int(input('Enter a number between -5 and 5: '))

  if number < -5 or number > 5:
    print(f"Number out of range: {number}")
    break
  sum_of_inputs += number

print(f"Sum of all your inputs: {sum_of_inputs}")

print("\n------ Example 13: while loop as counting operator -----")
index = 0
even_count = 0

while index < len(numbers):
  if numbers[index] % 2 == 0 and numbers[index]:
    even_count +=1
  index+=1

print(f"Even numbers count: {even_count}")