a = list(map(int, input("Nhập các số: ").split()))
tong_chan = 0
tong_le = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        tong_chan += a[i]
    else:
        tong_le += a[i]
print("Tổng số chẵn:", tong_chan)
print("Tổng số lẻ:", tong_le)
