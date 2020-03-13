sum = 0
count = 0
ave = 0
while True:
    n = input("Enter a number: ")
    if n =='done':
        break
    try:
        n =int(n)
        sum = sum + n
        count = count + 1
        ave = sum / count
    except:
        print("bad data")
        continue

print(sum, count, ave)
