a = list(map(int, input("Nhập các số: ").split()))
k = int(input("Nhập tổng k: "))
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == k:
            print("Cặp số:", a[i], a[j])
