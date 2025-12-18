a = list(map(int, input("Nhập các số: ").split()))
k = int(input("Nhập k: "))
n = len(a)
k = k % n
lan = 0
while lan < k:
    temp = a[n - 1]
    i = n - 1
    while i > 0:
        a[i] = a[i - 1]
        i -= 1
    a[0] = temp
    lan += 1
print("Danh sách sau khi dịch:", a)
