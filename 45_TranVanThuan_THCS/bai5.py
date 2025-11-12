# Nhập số tiền gửi ban đầu và lãi suất hàng năm
tien_gui = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): "))

# Chuyển lãi suất phần trăm sang dạng thập phân
lai_suat_nam /= 100

# Tính lãi sau 1 tháng, 2 quý, 3 năm (lãi đơn)
lai_1_thang = tien_gui * lai_suat_nam * (1 / 12)
lai_2_quy = tien_gui * lai_suat_nam * (6 / 12)   # 2 quý = 6 tháng
lai_3_nam = tien_gui * lai_suat_nam * 3

# In kết quả
print(f"Lãi nhận được sau 1 tháng: {lai_1_thang:.2f} VNĐ")
print(f"Lãi nhận được sau 2 quý: {lai_2_quy:.2f} VNĐ")
print(f"Lãi nhận được sau 3 năm: {lai_3_nam:.2f} VNĐ")
