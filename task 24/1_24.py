# подряд
f = open("1_24.txt")
k = 0
kmax = 0
s = f.readline()
for i in range(len(s)):
    if s[i] != 'z':
        k += 1
        if k > kmax: kmax = k
    else:
        k = 0
print(kmax)
f.close()

# два соседних различны
f = open("1_24.txt")
k = 1
kmax = 0
s = f.readline()
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        k += 1
        if k > kmax: kmax = k
    else:
        k = 1
print(kmax)
f.close()

# длина длинейшей различны
f = open("1_24.txt")
k = 1
kmax = 0
s = f.readline()
ch = s[0]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        k += 1
        if k > kmax:
            kmax = k
            ch = s[i]
    else:
        k = 1
print(ch, kmax)
f.close()

# длина длинейшей различны
f = open("1_24.txt")
s = f.readline()
k = ''
n = 0
nmax = 0
for i in range(1, len(s)):
    if '0' <= s[i] <= '9':
        k = k + s[i]
    elif k != "":
        n = int(k)
        if n % 2 != 0 and n > nmax:
            nmax = n
        k = ""
if k != "":
    n = int(k)
    if n % 2 != 0 and n > nmax:
            nmax = n
print(nmax)
f.close()


# Поиск КОТ
f = open("1_24.txt")
k = 0
kmax = 0
s = f.readline()
for i in range(len(s) - 2):
    if s[i] == "К" and s[i+1] == "О" and s[i+2] == "Т":
        k += 1
        if k > kmax:
            kmax = k
        else:
            k = 1
print(kmax)
f.close()

# Поиск КОТ, но не котик. Считаем КОТИК, а затем вычетаем
f = open("1_24.txt")
k = 0
k1 = 0
kmax = 0
s = f.readline()
for i in range(len(s) - 2):
    if s[i] == "К" and s[i+1] == "О" and s[i+2] == "Т":
        k += 1
for i in range(len(s) - 2):
    if s[i] == "К" and s[i + 1] == "О" and s[i + 2] == "Т" and s[i + 3] == "И" and s[i + 4] == "К":
        k1 += 1
print(k - k1)
f.close()
