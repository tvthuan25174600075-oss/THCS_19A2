a = list(map(int, input("Nhập các số: ").split()))
min_value = a[0]
for i in range(1, len(a)):
    if a[i] < min_value:
        min_value = a[i]

print("Số nhỏ nhất là:", min_value)
