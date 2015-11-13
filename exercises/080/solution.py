a = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    for j in range(i, 26):
        if (a[j] != a[i]):
            print(a[i] + a[j])
