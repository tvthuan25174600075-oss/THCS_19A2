du_lieu = {'A': 1, 'B': 2, 'C': 3}

dao_nguoc = {}

for khoa in du_lieu:
    gia_tri = du_lieu[khoa]
    dao_nguoc[gia_tri] = khoa

print(dao_nguoc)
