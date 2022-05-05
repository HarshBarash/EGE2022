a = 1
while True:
    for x in range(1, 1000000):
        if not ((x&25 != 0) <= ((x&19 == 0) <= (x&a != 0))):
            break
    else:
        print(a)
    a += 1
