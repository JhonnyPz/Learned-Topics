from typing import Counter


demo_list =[1, "Hello", 1.34, True, [1,2,3]]
color = ["Red", "Green", "Blue"]

number_List = list((1, 2, 3, 4))
print(number_List)

R = list(range(1, 9))
print(R)

print(type(color))
print(len(color))
print(color[2])
print("Green" in color)

print(color)
color[1] = "Grey"
print(color)

# Metodos print(dir(color))

color.append("Violet")
color.extend(["Orange", "Yello"])
color.insert(1, "Black")
print(color)

color.pop()
color.remove("Orange")
color.pop(1)
print(color)

color.sort()
print(color)
color.sort(reverse=True)
print(color)

print(color.index("Green"))
print(color.count("Red"))

color.clear()
print(color)
