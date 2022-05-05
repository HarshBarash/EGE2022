#неожиданный мув
s = "1" + '0' * 80
while '10' in s or '1' in s:
    if '10' in s:
        s = s.replace('10', '001', 1)
    elif '1' in s:
        s = s.replace('1', '000', 1)
print(len(str(s)))

#стандартное
s = "1" * 82
while '11111' in s or '888' in s:
    if '11111' in s:
        s = s.replace('11111', '88', 1)
    elif '888' in s:
        s = s.replace('888', '8', 1)
print(s)


#базовое
s = "7" * 79
while '7777' in s or '3333' in s:
    if '3333' in s:
       s =  s.replace('3333','77',1)
    else:
        s = s.replace('7777','33',1)
print(s)