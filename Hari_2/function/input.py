import aritmatika as f

# Input data
nama = input("Masukkan Nama: ")
BB = float(input("Masukkan Berat Badan (kg): "))
TB = float(input("Masukkan Tinggi Badan (meter): "))

# Calculate BMI
bmi = f.bmi(BB, TB)
print("BMI kamu adalah", bmi)

f.bmi_check(bmi)

# Save to file with timestamp
f.save_bmi(nama, bmi, BB, TB)
