x = float(input("First Grade: "))
y = float(input("Second Grade: "))

average = (x + y) / 2

if 90 <= average <= 100:
    print("A")
elif 70 <= average < 90:
    print("B")
elif 60 <= average < 70:
    print("C")
elif 0 <= average < 60:  
    print("FAIL!")
else:
    print("UNDEFINED")
