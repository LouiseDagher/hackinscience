a = range(0, 101)
b = 0
for i in a:
    if i % 2 == 0:
        b = i + b
print(b)
