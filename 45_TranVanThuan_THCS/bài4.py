n = int(input("Nhập n: "))
print("Các số nguyên tố nhỏ hơn", n, "là:")
for num in range(2, n):  
    for i in range(2, num):  
        if num % i == 0:      
            break
    else:
        print(num)
