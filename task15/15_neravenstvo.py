a = 1
while True:
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ((x + 2 * y < a) or (y > x) or (x > 20)):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1
