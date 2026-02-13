import math

def add_item(item, items=None):
    if items is None:
        items = []
    else:
        items = items.copy()
    items.append(item)
    return items
print(add_item(1))
print(add_item(2))

def check_sum():
    return math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9)
print(check_sum())

def countdown(n):
    if n < 0:
        return
    print(n)
    if n > 0:
        return countdown(n-1)
countdown(5)

def get_value():
    data = {"a": 1, "b": 2}
    return data.get("c", "Key not found")
print(get_value())

def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1
loop_example()

a, b, c = 1, 2, 3

def func():
    x = 5
    y = 10
    return x + y

print(func())

print(math.sqrt(16))
