a = list(map(int, input("Nhập các số: ").split()))
tang = True
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        tang = False
        break
if tang:
    print("Danh sách tăng dần")
else:
    print("Danh sách không tăng dần")
