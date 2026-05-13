import aritmatika as f
from datetime import datetime

# Input data
nama = input("Masukkan Nama: ")
BB = float(input("Masukkan Berat Badan (kg): "))
TB = float(input("Masukkan Tinggi Badan (meter): "))

# Calculate BMI
bmi = f.bmi(BB, TB)
print("BMI kamu adalah", bmi)

f.bmi_check(bmi)

# Save to file with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("bmi_data.txt", "a") as file:
    file.write(f"{timestamp} | {nama} | BB: {BB} kg | TB: {TB} m | BMI: {bmi:.2f}\n")

print(f"\nData berhasil disimpan ke bmi_data.txt")
