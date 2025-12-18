chuoi = input("Nhập chuỗi: ")
tan_suat = {}
for ky_tu in chuoi:
    if ky_tu in tan_suat:
        tan_suat[ky_tu] = tan_suat[ky_tu] + 1
    else:
        tan_suat[ky_tu] = 1
print(tan_suat)
