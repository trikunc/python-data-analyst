a = 100
b = 10**2
c = 101

a_apakah_sama_dengan_b = a == b
a_apakah_sama_dengan_c = a == c

# Sama Dengan

print(f"nilai a adalah {a}")
print(f"nilai b adalah {b}")
print(f"nilai c adalah {c}")


print(f"{a} apakah sama dengan {b}? {a_apakah_sama_dengan_b}")
print(f"{a} apakah sama dengan {c}? {a_apakah_sama_dengan_c}")

# Tidak Sama Dengan

a_apakah_tdk_sama_dengan_c = a != c
print(f"{a} apakah tidak sama dengan {c}? {a_apakah_tdk_sama_dengan_c}")

# Lebih Besar
a_lebih_besar_dari_b = a > b
print(f"{a} lebih besar dari {b}? {a_lebih_besar_dari_b}")

# Lebih Kecil
a_lebih_kecil_dari_c = a < c
print(f"{a} lebih kecil dari {c}? {a_lebih_kecil_dari_c}")

# Lebih Besar Sama Dengan
a_lebih_besar_sama_dengan_c = a >= c
print(f"{a} lebih besar sama dengan {c}? {a_lebih_besar_sama_dengan_c}")

# Lebih Kecil Sama Dengan
a_lebih_kecil_sama_dengan_c = a <= c
print(f"{a} lebih kecil sama dengan {c}? {a_lebih_kecil_sama_dengan_c}")
