BB = float(input("Masukkan Berat Badan (kg): "))
TB = float(input("Masukkan Tinggi Badan (meter): "))

# BMI = BB / (TB**2)
BMI = BB / (TB * TB)

print("BMI kamu adalah", BMI)

if BMI < 18.5:
    print("Kamu termasuk kategori kurus")
elif BMI >= 18.5 and BMI < 25:
    print("Kamu termasuk kategori normal")
elif BMI >= 25 and BMI < 30:
    print("Kamu termasuk kategori gemuk")
elif BMI >= 30 and BMI < 50:
    print("Kamu termasuk kategori obesitas")
else:
    print("ERROR")
