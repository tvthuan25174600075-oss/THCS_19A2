ten_nguon = "c:\\Users\\admin\\OneDrive\\Pictures\\Screenshots\\Ảnh chụp màn hình 2025-12-24 165516.png"
ten_dich = "c:\\Users\\admin\\OneDrive\\Pictures\\Screenshots\\SaoChep_Ảnh chụp màn hình 2025-12-24 165516.png"
try:
   
    with open(ten_nguon, "rb") as f_nguon, open(ten_dich, "wb") as f_dich:
        
        while True:
            khoi_du_lieu = f_nguon.read(1024)
            
            if not khoi_du_lieu:
                break
                
            f_dich.write(khoi_du_lieu)

    print(f"--- Đã sao chép thành công '{ten_nguon}' sang '{ten_dich}' ---")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tập tin nguồn '{ten_nguon}'.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")