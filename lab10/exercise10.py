colors = ['red','orange','olive','magenta','green']
user_selection = input("Enter a color: ").lower().strip()

for color in colors:
    if user_selection in colors:
        print(f"{user_selection} is in the list")
        break
    else:
        print(f"{user_selection} is NOT in the list")
        break