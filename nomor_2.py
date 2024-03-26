def kata2(kalimat, kata) :
    kalimat = kalimat.lower()
    kata = kata.lower()
    hasil = kalimat.count(kata)
    return hasil

kalimat = "saya harus makan, makan, dan makan"
kata = "makan"
hasil = kata2(kalimat, kata)
print(f"kata {kata} muncul {hasil} kali ")