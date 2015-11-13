import string
a = string.ascii_lowercase
for i in a:
    for j in a:
        if (j != i):
            print(str(i) + str(j))
