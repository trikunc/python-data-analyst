from datetime import datetime


def add(a=None, b=None):
    if a == None or b == None:
        print("parameter tidak lengkap")
        return

    total = a + b
    return total


def substract(a=None, b=None):
    if a == None or b == None:
        print("parameter tidak lengkap")
        return

    total = a - b
    return total


def bmi(berat=None, tinggi=None):
    if berat == None or tinggi == None:
        print("parameter tidak lengkap")
        return

    total = berat / (tinggi**2)
    return total


def bmi_check(bmi):
    if bmi < 18.5:
        print("Kamu termasuk kategori kurus")
    elif bmi >= 18.5 and bmi < 25:
        print("Kamu termasuk kategori normal")
    elif bmi >= 25 and bmi < 30:
        print("Kamu termasuk kategori gemuk")
    elif bmi >= 30 and bmi < 50:
        print("Kamu termasuk kategori obesitas")
    else:
        print("ERROR")


def save_bmi(name, bmi, BB, TB):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("Hari_2/function/bmi_data.txt", "a") as file:
        file.write(
            f"{timestamp} | {name} | BB: {BB} kg | TB: {TB} m | BMI: {bmi:.2f}\n"
        )

    print(f"\nData berhasil disimpan ke bmi_data.txt")
