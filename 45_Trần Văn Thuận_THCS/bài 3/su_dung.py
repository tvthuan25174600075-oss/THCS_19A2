# Import các hàm từ cả hai module trong package may_tinh
from may_tinh.co_ban import cong, tru
from may_tinh.nang_cao import luy_thua, can_bac_hai

# Thực hiện các phép tính để kiểm tra
print(f"Phép cộng: 10 + 5 = {cong(10, 5)}")
print(f"Phép trừ: 10 - 5 = {tru(10, 5)}")
print(f"Lũy thừa: 2 mũ 3 = {luy_thua(2, 3)}")
print(f"Căn bậc hai: Căn của 16 = {can_bac_hai(16)}")