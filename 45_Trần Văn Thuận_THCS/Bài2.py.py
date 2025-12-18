s = input("nhập chuỗi: ")
n=int(input("nhập n: "))
tu=" "
for c in s+" ":
    if c!=" ":
        tu=tu+c
    else:
        if len(tu)>n:
            print(tu)
        tu=" "
        