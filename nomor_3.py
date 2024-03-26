def hapus_spasi(kalimat) :
    kalimat = kalimat.split()
    kalimat_new = " ". join(kalimat)
    print(kalimat_new)

kalimat = "saya    tidak suka   memancing ikan     "
hapus_spasi(kalimat)