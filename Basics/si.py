p = float(input("Enter principal = "))
r = float(input("Enter rate = "))
t = float(input("Enter time = "))
si = (p*r*t)/100
print("The interest is =",si)
amount = si + p
print("The total amount is = ",amount)