num = 600851475143
i = 1
while num > 1:
    i += 1
    if i % 2 != 0 and (i % 3 != 0 and i > 3) and (i % 5 != 0 and i > 5) and (i % 7 != 0 and i > 7):
        if num % i == 0:
            num /= i
print(i)
