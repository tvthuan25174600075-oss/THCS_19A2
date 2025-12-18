a = list(map(int, input("Nhập các số: ").split()))
tong = 0
for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] % 5 != 0:
        tong += a[i]

print("Tổng các số chia hết cho 3 nhưng không chia hết cho 5:", tong)
