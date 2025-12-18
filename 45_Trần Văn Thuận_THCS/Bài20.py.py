du_lieu = {'A': 40, 'B': 60, 'C': 90, 'D': 30}

ket_qua = {}

for khoa in du_lieu:
    if du_lieu[khoa] > 50:
        ket_qua[khoa] = du_lieu[khoa]

print(ket_qua)
