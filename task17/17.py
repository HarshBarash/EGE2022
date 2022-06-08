# with open("17.txt") as f:
#     s = [int(x)for x in f]
#     res = []


k = 0
max1 = 0
for i in range(3201, 12877 + 1):
    if i % 4 == 0:
        if i % 7 != 0:
            if i % 11 != 0:
                if i % 19 != 0:
                    k += 1
                    if i > max1:
                        max1 = i
print(k, max1)

s = 0
max1 = 0
for i in range(3394, 8599 + 1):
    if i % 3 == 1:
        if i % 7 == 5:
            s += i
            if i > max1:
                max1 = i
print(max1, s)

with open("17.txt") as f:
    s = [int(x) for x in f]
    res = []
    max1 = 0
    for i in s:
        if i % 3 == 1:
            if i % 7 == 5:
                res.append(i)
                if i > max1:
                    max1 = i
print(max1, len(res))

k = 0
max1 = 0
for i in range(3439, 7410 + 1):
    if i % 2 != i % 6:
        if i % 9 == 0 or i % 10 == 0 or i % 11 == 0:
            k += 1
            if i > max1:
                max1 = i
print(k, max1)

k = 0
max1 = 0
for i in range(3439, 7410 + 1):
    if i % 2 != i % 6:
        if i % 9 == 0 or i % 10 == 0 or i % 11 == 0:
            k += 1
            if i > max1:
                max1 = i
print(k, max1)

k = 0
max1 = 0
for i in range(3439, 7410 + 1):
    if i < 6 ** 5:
        if (i // 6 % 6 == 1) and (i % 6 == 3 or i % 6 == 4):
            k += 1
            if i > max1:
                max1 = i
print(k, max1)

k = 0
min1 = 10000
for i in range(3905, 7998 + 1):
    if (i // 100 % 10 >= 2) and (i // 100 % 10 <= 6):
        if (i // 10 % 10 != 0) and (i // 10 % 10 != 5):
            k += 1
            if i < min1:
                min1 = i
print(k, min1)

with open("17.txt") as f:
    s = [int(x) for x in f]
    res = []
    for i in s:
        if str(i).count('0') >= 2 and i % 7 == 0:
            res.append(i)
print(max(res), len(res))

with open("17.txt") as f:
    s = [int(x) for x in f]
    res = []
    for i in range(1, len(s)):
        if (abs(s[i]) % 10 == 7 or abs(s[i - 1]) % 10 == 7) and (s[i] + s[i - 1]) % 12 == 0:
            res.append((s[i] + s[i - 1]))
print(len(res), max(res))

with open("17.txt") as f:
    s = [int(x) for x in f]
    res = []
    for i in range(0, len(s) - 1):
        for j in range(i + 1, len(s)):
            if ((s[i] - s[j] % 2 == 0) and (s[i] % 19 == 0 or s[j] % 19 == 0)):
                res.append(s[i] - s[j])
print(len(res), max(res))

# тройки
with open("17.txt") as f:
    s = [int(x) for x in f]
    res = []
    for i in range(2, len(s)):
        if (s[i - 2] < (sum(s) // len(s)) and '9' in str(s[i - 2]) and '9' in str(s[i - 1]) and '9' in str(s[i])) or \
                (s[i - 1] < (sum(s) // len(s)) and '9' in str(s[i - 2]) and '9' in str(s[i - 1]) and '9' in str(
                    s[i])) or \
                (s[i] < (sum(s) // len(s)) and '9' in str(s[i - 2]) and '9' in str(s[i - 1]) and '9' in str(s[i])):
            res.append(s[i] + s[i - 1] + s[i - 2])
print(len(res), max(res))

with open("17.txt") as f:
    s = [int(x) for x in f]
    res = []
    for i in range(len(s) - 1):
        if abs(s[i]) % 3 == 0 or abs(s[i - 1]) % 3 == 0:
            res.append((s[i] + s[i - 1]))
print(len(res), max((res)))


with open("17.txt") as f:
    s = [int(x) for x in f]
    res = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if (s[i] - s[j]) % 2 == 0 and ((s[i]) % 31 == 0 or (s[j]) % 31 == 0):
                res.append((s[i] + s[j]))
print(len(res), max(res))