import json

data = {
    "nama depan": "alice",
    "nama belakang": "wonder",
    "alamat": "bumijo",
    "umur": 24,
    "hobby": ["padel", "tenis", "tenis meja"],
}

# print(data["alamat"])

# data["alamat"] = "Jogja"

# print("\nsetelah diubah")
# print(data["alamat"])

BigData = [
    {
        "nama depan": "alice",
        "nama belakang": "wonder",
        "alamat": "bumijo",
        "umur": 24,
        "hobby": ["padel", "tenis", "tenis meja"],
    },
    {
        "nama depan": "bob",
        "nama belakang": "marley",
        "alamat": "jetis",
        "umur": 20,
        "hobby": ["renang", "joging", "masak"],
    },
    {
        "nama depan": "farah",
        "nama belakang": "wonder",
        "alamat": "tugu",
        "umur": 21,
        "hobby": ["mukbang", "traveling", "membaca"],
    },
]

BigData.append(
    {
        "nama depan": "edi",
        "nama belakang": "wonder",
        "alamat": "tugu",
        "umur": {
            "tahun": 21,
            "bulan": 3,
            "hari": 15,
        },
        "hobby": ["mukbang", "traveling", "membaca"],
    }
)

print(json.dumps(BigData, indent=4))
