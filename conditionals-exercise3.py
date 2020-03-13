grade = input("Enter Grade:")
try:
    grade = float(grade)
except:
    grade = -1
if grade < 0:
        print("Not a grade.")
elif float(grade) > 1.0:
    print("Doesn't work like that unfortunately.")
elif float(grade) >= 0.9:
    print("A")
elif float(grade) >= 0.8:
    print("B")
elif float(grade) >= 0.7:
    print("c")
elif float(grade) >= 0.6:
    print("D")
elif float(grade) < 0.6:
    print("F")
