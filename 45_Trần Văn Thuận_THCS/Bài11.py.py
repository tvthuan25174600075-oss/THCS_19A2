a = list(map(int, input("Nhập các số: ").split()))

i = 0
j = len(a) - 1

while i < j:
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    i += 1
    j -= 1

print("Danh sách sau khi đảo:", a)
