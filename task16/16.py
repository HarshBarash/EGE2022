# 1
# def F(n):
#     if n < 5:
#         return F(3*n) + F(n+3) + F(n+1)
#     else:
#         return n // 2
#
# print(F(2))


# 2
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1 and n % 2 == 0:
#         return n*n+F(n-1)
#     elif n > 1 and n % 2 != 0:
#         return F(n-1) + 2*F(n-2)
# print(F(23))

# 3
# def F(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return F(n-1)-n*G(n-1)
#
# def G(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return F(n-1) + 2*G(n-1)
#
# print(G(18))

# 4
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 3*F(n-1)+G(n-1)-n+5
#
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1) + 3*G(n-1) - 3*n
#
# print( (F(14) + G(14)))

# 5
# def F(n):
#     if n > 0:
#         G(n - 1)
#
# def G(n):
#     print("*")
#     if n > 1:
#         F(n - 3)
#
# F(11)

# 6
# k = 0
# def F(n):
#     global k
#     k += 1
#     if n >= 1:
#         k +=1
#         F(n-1)
#         F(n//2)
#
# F(140)
# print(k)

# 7
# def F(n):
#     if n > 15:
#         return n * n - 5
#     if n <= 15:
#         return n * F(n+2) + n + F(n+3)
#
# #debug - print(F(1))
#
# s = 0
# x = F(1)
# while x > 0:
#     s = s + x % 10
#     x = x // 10
# print(s)

# 8
# def F(n):
#     if n > 25:
#         return 2 * n * n * n + 1
#     if n <= 25:
#         return F(n + 2) + 2 * F(n + 3)
#
# k = 0
# for n in range(1, 1001):
#     if F(n) % 11 == 0:
#         k += 1
# print(k)

# 9
# def F(n):
#     if n > 25:
#         return n*n + 4*n+3
#     if n <= 25 and n % 3 == 0:
#         return F(n+1)+2*F(n+4)
#     if n <= 25 and n % 3 != 0:
#         return F(n+2) + 3*F(n+5)
#
# k = 0
# for n in range(1,1001):
#     x = F(n)
#     s = 0
#     while x > 0:
#         s = s + x % 10
#         x = x // 10
#     if s == 24:
#         k +=1
# print

#10
# def F(n, m):
#     if m == 0:
#         return n
#     else:
#         return F(m,n % m)
#
# #Различных значений n, поэтому множество
# s = set()
# for n in range(100, 1001):
#     for m in range(100, 1001):
#         if F(n, m) == 30:
#             s.add(n)
# print(len(s))

#11
# def F(n):
#     if n <= 2:
#         return 2
#     if n > 2:
#         return F(n-1) + 2*F(n-2)
#
# print(F(5))

#12
# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return F(n-2) * n
#
# print(F(7))

#13
def F(n):
    print(n)
    if n < 4:
        F(n + 1)
        F(n + 3)

print(F(1))