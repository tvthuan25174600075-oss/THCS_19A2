from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri


so = [5, 2, 9, 1, 7]
print(f"Danh sách gốc: {so}")
print(f"Sau khi sắp xếp: {sap_xep_tang_dan(so)}")

my_info = {"ten": "Gemini", "ngon_ngu": "Python", "nam": 2025}
key = "ngon_ngu"
print(f"Giá trị của khóa '{key}' là: {lay_gia_tri(my_info, key)}")