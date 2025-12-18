a = list(map(int, input("Nhập các số: ").split()))
kq = []
for i in range(len(a)):
    trung = False
    for j in range(len(kq)):
        if a[i] == kq[j]:
            trung = True
            break
    if trung == False:
        kq.append(a[i])

print("Danh sách sau khi loại trùng:", kq)
