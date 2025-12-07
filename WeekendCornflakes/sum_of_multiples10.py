sum = 0
for integer in range(1, 20001):
    if integer % 10 == 0:
        sum += integer
print(sum)
