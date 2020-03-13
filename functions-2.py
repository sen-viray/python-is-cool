def computegrade(grade):
    if grade < 0:
            return str("Not a grade.")
    elif float(grade) > 1.0:
        return str("Doesn't work like that unfortunately.")
    elif float(grade) >= 0.9:
        return str("A")
    elif float(grade) >= 0.8:
        return str("B")
    elif float(grade) >= 0.7:
        return str("c")
    elif float(grade) >= 0.6:
        return str("D")
    elif float(grade) < 0.6:
        return str("F")


grade = input("Enter Grade:")
try:
    grade = float(grade)
except:
    grade = -1
print(str(computegrade(grade)))
