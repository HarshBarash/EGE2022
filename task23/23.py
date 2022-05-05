#база
def f(x,y):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        return f(x + 1, y) + f(x * 2, y)
print(f(1, 10) * f(10,20))


def f(x,y):
    if x == y:
        return 1
    elif x>y:
        return 0
    else:
        return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)
print(f(5, 9) * f(9, 15) * f(15,17))

#не учитывая
def f(x, y):
    if x==y:
        return 1
    elif x>y or x == 27:
        return 0
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
print(f(2, 15) * f(15, 39))

#вычитая
def f(x, y):
    if x==y:
        return 1
    elif x<y:
        return 0
    else:
        return f(x - 1, y) + f(x - 5, y)
print(f(17, 1))

#крылов
def f(x, y):
    if x==y:
        return 1
    elif x<y:
        return 0
    else:
        return f(x - 1, y) + f(x // 3, y)
print(f(37, 10) * f(10, 2))