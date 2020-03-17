### TIDAK BISA DI RUN ###
if target in arrayTempatYangDicari:
    print("targetnya terdapat di array itu")
else:
    print("targetnya tidak terdapat di array itu")
### TIDAK BISA DI RUN ###

#### 4.1 LINEAR SEARCH ####
## LATIHAN 1
def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

## import modul 2
import modul2 as md

## LATIHAN 2
c0 = md.MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1 = md.MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = md.MhsTIF('Ahmad', 2, 'Surakarta', 250000)
c3 = md.MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4 = md.MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = md.MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = md.MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = md.MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = md.MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = md.MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = md.MhsTIF('Khalid', 29, 'Purwodadi', 265000)

## LALU KITA MEMBUAT DAFTAR MAHASISWA DALAM BENTUK LIST SEPERTI INI:

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

target = 'Klaten'
for i in Daftar:
        if i.kotaTinggal == target:
            print(i.nama + 'tinggal di' + target)

## LATIHAN 3
def cariTerkecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan [0]
    for i in range(1, n):
        if kumpulan[i] < terkecil:
            terkecil = kumpulan[i]
    return terkecil

## Bagaimana programnya jika kita ingin mencari mahasiswa(dari class MhsTIF di atas) yang uang sakunya terkecil?
def kecil(Daftar):
    minim = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku < minim:
            minim = i.uangSaku
            if i.uangSaku == minim:
                nama = i.nama
    return nama, minim
print(kecil(Daftar))

## Bagaimana kalau yang terbesar?
def besar(Daftar):
    maxim = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku > maxim:
            maxim = i.uangSaku
            if i.uangSaku == maxim:
                nama = i.nama
    return nama, maxim
print(besar(Daftar))

## Bagaimanakah programnya jika kita ingin mencari semua mahasiswa yang uang sakunya kurang dari 250ribu?
def kurang(Daftar):
    a=[]
    for i in Daftar:
        if i.uangSaku < 250000:
            a.append(i.nama)
    return a
print(kurang(Daftar))

## Bagaimana kalau lebih?
def lebih(Daftar):
    a = []
    for i in Daftar:
        if i.uangSaku >= 250000:
            a.append(i.nama)
    return a
print(lebih(Daftar))

#### 4.2 BINARY SEARCH ####
##LATIHAN 4
def binSe(kumpulan, terget):
    #mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1

    #secara berulang belah runtutan itu menjadi separuhnya
    #   sampai targetnya ditemukan
    while low <= high:
            #temukan pertengahan runtut itu
        mid = (high + low) // 2
            #Apakah pertengahanya semua target?
        if kumpulan[mid] == target:
            return True
            #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
            #atau targetnya ada di sebelah kananya?
        else:
            low = mid + 1
        #jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False
kumpulan = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 6
print(binSe(kumpulan,target))
kumpulan = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 7
print(binSe(kumpulan,target))

##Dapatkah kamu mengubah programnya agar dia mengembalikan index-nya kalau targetnya ditemukan,
##dan mengembalikan False kalau target tidak ditemukan

def binSe(kumpulan, target):
    a=[]
    low = 0
    high = len(kumpulan) - 1
    while(low<=high):
        mid = (low+high)//2
        if(kumpulan[mid] == target):
            a.append(kumpulan.index(target))
            i=kumpulan.index(target)-1
            j = kumpulan.index(target) + 1
            while target == kumpulan[i]:
                a.append(i)
                i-=1
            while target == kumpulan[j]:
                a.append(j)
                j+=1
            return a
        elif(target<kumpulan[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return False

kumpulan = [2,3,3,3,4,4,4,4,4,5,6,6,8,9,9,10,11,12,13,13,14]
target = 6
print(binSe(kumpulan,target))
kumpulan = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 7
print(binSe(kumpulan,target))
