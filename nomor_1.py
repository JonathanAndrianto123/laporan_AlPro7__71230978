def anagram(kata1, kata2) :
    for i in range(0, len(kata2) - 1):
        if kata1[i] in kata2 :
            hasil = "benar"
        else :
            hasil = "salah"
    if hasil == "benar" :
        print("anagram")
    else :
        print("bukan")

kata1 = input("masukkan kata pertama = ")
kata2 = input("masukkan kata kedua = ")
anagram(kata1, kata2)