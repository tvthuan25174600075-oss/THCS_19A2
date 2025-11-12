# Nhập độ dài cạnh đáy và chiều cao
day = float(input("Nhập độ dài cạnh đáy (đơn vị cm): "))
chieu_cao = float(input("Nhập chiều cao (đơn vị cm): "))

# Tính diện tích tam giác
dien_tich = 0.5 * day * chieu_cao

# In kết quả
print(f"Diện tích tam giác là: {dien_tich:.2f} cm²")