# Nhập số tiền bằng VNĐ
tien_vnd = float(input("Nhập số tiền (VNĐ): "))

# Tỷ giá quy đổi
ty_gia = 24500  # 1 USD = 24.500 VNĐ

# Quy đổi sang USD
tien_usd = tien_vnd / ty_gia

# In kết quả (làm tròn đến 2 chữ số thập phân)
print(f"Số tiền tương đương: {tien_usd:.2f} USD")