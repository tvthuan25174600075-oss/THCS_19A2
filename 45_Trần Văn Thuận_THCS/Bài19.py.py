sinh_vien = {
    'A': 8,
    'B': 9,
    'C': 8,
    'D': 9
}

nhom_theo_diem = {}

for ten in sinh_vien:
    diem = sinh_vien[ten]

    if diem in nhom_theo_diem:
        nhom_theo_diem[diem].append(ten)
    else:
        nhom_theo_diem[diem] = [ten]

print(nhom_theo_diem)
