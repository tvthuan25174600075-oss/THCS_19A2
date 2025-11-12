# Nhập tổng số kẹo và số học sinh
tong_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập số học sinh: "))

# Tính số kẹo mỗi học sinh nhận được
keo_moi_hs = tong_keo // so_hoc_sinh  # phép chia lấy phần nguyên

# Tính số kẹo còn thừa
keo_con_thua = tong_keo % so_hoc_sinh  # phép chia lấy phần dư

# In kết quả
print(f"Mỗi học sinh nhận được: {keo_moi_hs} viên kẹo")
print(f"Số kẹo còn thừa: {keo_con_thua} viên")