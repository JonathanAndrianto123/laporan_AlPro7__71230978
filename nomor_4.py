def perbandingan_kata(kalimat) :
    hasil = kalimat.split(" ")
    hasil.sort(key = len)
    terpendek = hasil[0]
    terpanjang = hasil[len(hasil) - 1]
    print(f"terpendek = {terpendek}")
    print(f"terpanjang = {terpanjang}")

kalimat = input("masukkan kalimat = ")
perbandingan_kata(kalimat)