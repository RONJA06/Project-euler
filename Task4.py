poli = 0
for i in range(1000):
    for j in range(1000):
        num = i * j
        if num == int(str(num)[::-1]) and num > poli:
            poli = num
print(poli)
