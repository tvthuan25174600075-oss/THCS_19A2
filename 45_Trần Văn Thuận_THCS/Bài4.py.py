a = list(map(int, input("Nhập các số: ").split()))
max1 = a[0]
max2 = a[0]
for i in range(1, len(a)):
    if a[i] > max1:
        max2 = max1
        max1 = a[i]
    elif a[i] != max1 and a[i] > max2:
        max2 = a[i]
if max1 == max2:
    print("Không tồn tại giá trị lớn thứ hai")
else:
    print("Giá trị lớn thứ hai là:", max2)
