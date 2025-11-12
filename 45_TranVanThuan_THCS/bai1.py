# Nhập giá sản phẩm và số lượng
gia = float(input("Nhập giá sản phẩm (VNĐ): "))
so_luong = int(input("Nhập số lượng mua: "))

# Tính tổng chi phí
tong_chi_phi = gia * so_luong

# Tính thuế VAT 10%
thue_vat = tong_chi_phi * 0.10

# Tính tổng tiền phải trả
tong_tien = tong_chi_phi + thue_vat

# In kết quả, làm tròn đến 2 chữ số thập phân
print(f"Tổng tiền phải trả (đã gồm VAT): {tong_tien:.2f} VNĐ")
