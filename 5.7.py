x = int(input())
y = int(input())
r = int(input())
if x**2 + y**2 <= r**2:
    print(f"Точка ({x}, {y}) принадлежит кругу с радиусом {r}")
else:
    print(f"Точка ({x}, {y}) не принадлежит кругу с радиусом {r}")