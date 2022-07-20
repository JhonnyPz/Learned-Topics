print("AAA")

def hello():
    print("HELLO WORD")

hello()

def hello_name(name):
    print("HELLO ", name)

hello_name("PEPE")
hello_name("TOMAS")

def calculador(A1,A2):
    return A1 + A2

print(calculador(20,4))
print(calculador(600,400))


add = lambda A1, A2: A1 + A2

print(add(10,20))
