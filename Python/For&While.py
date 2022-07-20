foods = ["Apples", "Bread", "Cheese", "Milk", "Bananas"]

for food in foods:
    if food == "Cheese":
        print("{0}: You have to buy this" .format(food))
        break
    print(food)


for food in foods:
    if food == "Cheese":
        continue
    print(food)


for letter in "Hello ":
    print(letter)

#######################################

count = 4

while count <= 10:
    print(count)
    count = count + 1