du_lieu = {'A': 10, 'B': 25, 'C': 15}
khoa_lon_nhat = None
gia_tri_lon_nhat = None
for khoa in du_lieu:
    if gia_tri_lon_nhat is None or du_lieu[khoa] > gia_tri_lon_nhat:
        gia_tri_lon_nhat = du_lieu[khoa]
        khoa_lon_nhat = khoa

print("Khóa có giá trị lớn nhất:", khoa_lon_nhat)
