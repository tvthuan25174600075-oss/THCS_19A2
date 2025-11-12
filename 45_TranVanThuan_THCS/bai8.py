# Nhập cân nặng (kg) và chiều cao (m)
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

# Tính BMI
bmi = can_nang / (chieu_cao * chieu_cao)

# In kết quả, làm tròn đến 2 chữ số thập phân
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
