grade = input("Enter Grade:")
try:
    grade = str(grade)
except:
    grade = -1
if str(grade) > 1.0:
    print("Error")
elif str(grade) >= 0.9:
    print("A")
elif str(grade) >= 0.8:
    print("B")
