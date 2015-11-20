def sort_a_list(a):
    OK = False
    while OK is False:
        OK = True
        for i in range(0, len(a) - 1):
            if a[i] < a[i + 1]:
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
                OK = False
    return(a)
