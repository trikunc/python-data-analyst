from datetime import datetime


def sapa():
    print("HELLO HAI")


def sapa_nama(nama=None):
    if nama is None:
        print("Silakan masukkan nama")
        return

    print(f"HELLO {nama}")


# print("Sebelum memanggil fungsi")
sapa()
sapa_nama("kuncoro")

sapa_nama()

# print(datetime.now())
