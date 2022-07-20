# > < >= >= == 

x = 20

if x  < 30:
    print("x is less than 30")

if x == 20:
    print("x is 20")

if x > 30:
    print("A1")
else:
    print("B1")

#############

y = "Red"

if y == "Violet":
    print("Violet")
elif y == "Red":
    print(y)
else:
    print("NOT")

##############

name = "John"
lastname = "carter"

if name == "John":
    if lastname == "Carter":
        print("You are John Carter")
    else:
        print("You are not Jhon Carte")
else:
    print("You are not John")


###############

E1 = 10

if E1 > 5 and E1 < 10:
    print("A1")
if E1 > 5 or E1 <=10:
    print("B1")
if (not(E1 == 0)):
    print("C1")