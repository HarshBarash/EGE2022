for i in range(1, 100):
    x = i
    q = 9
    l = 0
    while x>= q:
        l = l + 1
        x = x - q
    m = x
    if m < l:
        m = l
        l = x
    if l == 4 and m == 5:
        print(i)