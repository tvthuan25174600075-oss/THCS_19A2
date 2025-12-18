a = list(map(int, input("Nhập các số: ").split()))
for x in a:
    if x < 2:
        continue
    dem = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem += 1
    if dem == 2:
        print(x, "là số nguyên tố")
