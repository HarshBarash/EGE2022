for i in range(1, 100):
    x = i
    q = 9
    l = 0
    while x >= q:
        l = l + 1
        x = x - q
    m = x
    if m < l:
        m = l
        l = x
    if l == 4 and m == 5:
        print(i)

# смотри на условие, если что-то не так
for i in range(5, 1000):
    x = i
    a = 7 * x + 27
    b = 7 * x - 33
    while a != b:  # сюда;)
        if a > b:
            a -= b
        else:
            b -= a
    if a == 15:
        print(i)
