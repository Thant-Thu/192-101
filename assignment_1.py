x = 8
if x % 2 == 0:
    print('even')
else:
    print('odd')

score = 72
if score >= 80:
    print('A')
elif score >= 70:
    print('B')
elif score >= 50:
    print('C')
else:
    print('F')

a = 5
b = 5
if a > b:
    print('a wins')
elif a < b:
    print('b wins')
else:
    print('tie')

age = 20
if age >= 18 and age < 60:
    print('adult')
else:
    print('not in range')

x = 7

if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")

n = 24

if n % 2 == 0 and n % 3 == 0:
    print("divisible by 6")
elif n % 2 == 0:
    print("even only")
else:
    print("odd")

cf = int(input("enter currenf:"))
tf = int(input("enter targetf:"))

if tf == 13:
    print("Floor 13 is skipped. Redirecting to floor 14.")
    tf = 14

if cf < tf:
   r = tf - cf
   print(f"going up to {r} floors")

elif cf > tf:
   d = cf - tf
   print(f"going down to {d} floors")

else:
  print("You are on the same floor.")

age = int(input("Enter age: "))
ticketp = 120

if age > 0:
    if age <= 12:
        weekend = input("Weekend? Yes/No: ")
        if weekend == "Yes":
            ticketp = (120 / 2) + 30
        else:
            ticketp = 120 / 2
        print(f"{ticketp} baht")
    elif age < 60:
        weekend = input("Weekend? Yes/No: ")
        if weekend == "Yes":
            ticketp = 120 + 30
        else:
            ticketp = 120
        print(f"{ticketp} baht")
    else:
        weekend = input("Weekend? Yes/No: ")
        if weekend == "Yes":
            ticketp = 80 + 30
        else:
            ticketp = 80
        print(f"{ticketp} baht")
else:
    print("Invalid age")

b = int(input("Balance:"))
a = int(input("Amount:"))
if a > b:
   print("Insufficient balance")
else:
     if a % 100 == 0:
        if a >= 20000:
          print("Over daily limit")
        else:
             nb = b - a
             print(f"a {a} baht.")
             print(f"New Balance 1{nb}")

units = float(input("Enter units:"))
if units <= 150:
   tb = units * 3
   print(f"Total Bills: {tb} baht")
elif units > 400:
   tb = 150*3 + (units-150)*4 + (units-400)*5
   print(f"Total Bills: {tb} baht")
else:
     tb = 150*3 + (units-150)*4

     print(f"Total Bills: {tb} baht")
