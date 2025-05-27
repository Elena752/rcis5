import random
x = []
for i in range(10):
    num = random.randint(-100, 100) * 2
    x.append(num)
x.sort()
print(x)