print(f"----- Example 1: if Statement -----")

age = int(input('Enter your age: '))
ageCode = 123

if age < 0 or age > 130:
  print('Invalid age')
elif age <= 20:
  print('You are a minor')
elif age <= 64:
  print('You are an adult')
else: 
  # age must be between 65 and 130 inclusive here
  print('You are a senior citizen')

print(f"----- Example 4: and Operator -----")
temp = 90
humidity = 60

if 80 <= temp <= 90 and humidity < 80:
  print('The weather is pleasant')
else:
  print('The weather is not ideal')
  
print(f"----- Example 5: or Operator -----")
day = "Monday"
is_holiday = True

if day == 'Saturday' or day == 'Sunday' or is_holiday:
  print('You can relax today')
else:
  print('It is a workday')

print(f"----- Example 6: Nested Conditional Statement -----")
num = int(input('Enter a number: '))

if (num >= 0):
  if num == 0:
    print('The number is zero')
  else:
    print(f'{num} is positive')
else:
  print(f'{num} is negative')

print(f"----- Example 7: Nested Conditional Statement -----")
# username validation: username be at least 3 characters long
username = input('Enter a username: ').strip()
username_length = len(username)

if username_length >= 3:
  index_of_whitespace = username.find(' ')
  
  if index_of_whitespace == -1:
    print(f'{username} is a valid username')
  else:
    print(f'{username} is invalid! (no whitespace allowed)')
else:
  print(f'{username} has less than 3 characters')

print(f"----- Example 8: match-case(switch-case) -----")
response_code = 800

match response_code:
  case 200:
    print(f"Code {response_code}: OKAY")
  case 400:
    print(f"Code {response_code}: SERVER CAN'T UNDERSTAND")
  case 401 | 403:
    print(f"Code {response_code}: SERVER REFUSED TO SEND BACK")
  case 404:
    print(f"Code {response_code}: SERVER CANNOT FIND")
  case _:
    print(f"Code {response_code}: INVALID CODE")