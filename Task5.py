def smallest_divisible(num1, num2):
    num = num1
    while True:
        if num2 == 1:
            return num
        if num % num2 == 0:
            return smallest_divisible(num, num2 - 1)
        num += num1


print(smallest_divisible(20, 19))
