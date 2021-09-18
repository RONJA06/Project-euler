num = [3]
i = 3
le = len(num)
while le < 10001:
    i += 2
    isSimple = True
    for j in num:
        if j ** 2 > i:
            break
        else:
            if i % j == 0:
                isSimple = False
                break
    if isSimple:
        num.append(i)
        le += 1
print(num[-1])
