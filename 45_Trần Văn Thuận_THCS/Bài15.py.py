a = list(map(int, input("Nhập các số: ").split()))
max_dem = 0
gia_tri = a[0]
for i in range(len(a)):
    dem = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            dem += 1
    if dem > max_dem:
        max_dem = dem
        gia_tri = a[i]
print("Phần tử xuất hiện nhiều nhất:", gia_tri)
