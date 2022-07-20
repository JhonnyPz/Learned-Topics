product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "first_name": "Ryan",
    "Last_name": "Ray"
}

print(type(product))
print(person.keys())
print(person.items())

person.clear()
print(person)
del person

product = [
    {"name": "lapto", "price": 3.99},
    {"name": "lapiz", "price": 0.54}
]