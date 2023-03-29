def greetHello(name, ending):
    print("Hello " + name)
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print(ending)

def letterGenerator(name, date):
    st = f"Hi mam, \nThis is {name} and I will not come to college on {date}"
    print(st)

def average(a, b):
    return(a+b)/2


print("Executing Function...")
greetHello("Mahmud", "Thank You")
greetHello("Mahmud", "Thanks!!")
letterGenerator("Mahmud", "20th march")
letterGenerator("Mahmud", "25th march")
print(average(34, 45))

print("done")