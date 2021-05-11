#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Sets

'''Suatu program TV membuat acara challenge belanja selama 15 menit yang diikuti 2 peserta. Dalam acara tersebut,
barang yang sama-sama dibeli oleh kedua peserta dapat dibawa pulang. Maka dari itu diperlukan program daftar barang
yang sama dari kedua peserta.'''

def cekbarang():
    peserta1 = set()
    peserta2 = set()
    x = int(input("Masukkan jumlah barang yang dibeli peserta pertama : "))
    y = int(input("Masukkan jumlah barang yang dibeli peserta kedua : "))
    print("Barang - barang yang dibeli peserta pertama : ")
    for x in range(0,x):
        peserta1.add(input())
    print("Barang - barang yang dibeli peserta kedua : ")
    for x in range(0,y):
        peserta2.add(input())
    print("Jadi barang yang sama adalah :", peserta1 & peserta2)

cekbarang()