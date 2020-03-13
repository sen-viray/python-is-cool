hours = input("Enter Hours: ")
try:
    hours = int(hours)
except:
    hours = -1
if hours < 0 :
    print("Nice try, won't work though.")
    pay = 0
rate = input("Enter Rate: ")
try:
    rate = int(rate)
except:
    rate = -1
if rate < 0 :
    print("Already told you, that trick won't work. Try again.")
    pay = 0
if int(hours) > 40 :
    pay = int(hours) * (int (rate) * 1.5)
else :
    pay = int(hours) * int(rate)

print("Pay: ", pay)
