chuoi = input("Nhập chuỗi: ")
chuoi_moi = ""
ky_tu_truoc = ""
for ky_tu in chuoi:
    if ky_tu != " ":
        chuoi_moi = chuoi_moi + ky_tu
        ky_tu_truoc = ky_tu
    else:
        if ky_tu_truoc != " " and chuoi_moi != "":
            chuoi_moi = chuoi_moi + " "
            ky_tu_truoc = " "

print(chuoi_moi)
