a = list(map(int, input("Nhập các số: ").split()))
duong = 0
am = 0
khong = 0
for i in range(len(a)):
    if a[i] > 0:
        duong += 1
    elif a[i] < 0:
        am += 1
    else:
        khong += 1

print("Số dương:", duong)
print("Số âm:", am)
print("Số bằng 0:", khong)
