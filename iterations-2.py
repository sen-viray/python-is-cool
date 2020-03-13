max = 0
min = 100000000000000
while True:
    n = input("Enter a number: ")
    if n =='done':
        break
    try:
        n =int(n)
        if n > max:
            max = n
        if n < min:
            min = n
    except:
        print("bad data")
        continue

print("Minimum:", min, "Maximum: ", max)
