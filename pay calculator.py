hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
if int(hours) > 40 :
    pay = int(hours) * (int (rate) * 1.5)
else :
    pay = int(hours) * int(rate)

print("Pay: ", pay)
