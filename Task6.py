sum_squares = 0
square_sum = 0
for i in range(101):
    sum_squares += i * i
for j in range(101):
    square_sum += j
square_sum *= square_sum
print(square_sum - sum_squares)
