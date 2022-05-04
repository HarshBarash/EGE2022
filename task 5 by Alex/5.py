def appendN(N):
    count_1 = N.count('1')
    count_0 = N.count('0')
    if count_1 == count_0:
        N += N[-1]
    elif count_1 < count_0:
        N += '1'
    elif count_0 < count_1:
        N += '0'
    return N


def F(N):
    N = bin(N).replace('0b', '') # перевод в двоичную
    R = appendN(appendN(appendN(N))) # так как шаг надо повторить 1+2 раза
    return int(R, 2) # перевод в десятичную


for i in range(105, 1000):
    if F(i) % 4 == 0:
        print(i)
        break