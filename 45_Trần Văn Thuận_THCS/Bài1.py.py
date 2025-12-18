x=input("nhập chuỗi: ")
chu=0
so=0
dac_biet=0
for i in x:
    if "a"<=i<="z" or "A"<=i<="Z":
        chu+=1
    elif "0"<=i<="9":
        so+=1
    else:
        dac_biet+=1
print("chữ cái:", chu) 
print("chữ số: ", so)
print("ký tự đặc biệt: ", dac_biet)

