### 6.1 Menggabungkan dua list yang sudah urut ###
P = [2,8,15,23,37]
Q = [4,6,15,20]
R = gabungkanDuaListUrut(P, Q)
print(R)

def gabungkanDuaListUrut(A, B):
    la = len(A)
    lb = len(B)
    C = list()       #C adalah list baru
    i = 0
    j = 0

    #Gabungkan keduanya sampai salah satu kosong
    while i < la and j < lb:
        if A[i]< B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
            
    while i < la:        #Jika A mempunyai sisa
        C.append(A[i])   # tumpukan ke list baru itu
        i+=1             # satu demi satu
        
    while j < lb:        #Jika A mempunyai sisa 
        C.append(B[j])   # tumpukan ke list baru itu
        j+=1             # satu demi satu
        
    return c

print("P =", P)
print("Q = ",Q)
print("gabung dan urutkan q")
print(gabungkanlisturut(P,Q))


### 6.2 Merge Sort ###
def mergeSort(A):
    if len(A) > 1:
        mid = len (A) // 2          # Membelah list
        separuhKiri = A[:mid]       # Slicing ini langkah yang expensive sebenarnya
        separuhKanan = A[mid:]      # bisakah kamu membuatnya lebih baik?
        
        mergesort(separuhKiri)      # Ini rekursi. memanggil lebih lanjut mergeSort
        mergesort(separuhKanan)     # untuk separuhKiri dan separuhKanan
        
        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k]= separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k + 1
            
        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1
            
        while j< len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1


alist = [54,26,93,17,77,31,44,55,20]
print("===================================")
print("a = ",alist)
mergesort(alist)
print("urutkan a : ",alist)
print("===================================")


### 6.3 Quick Sort ###
def quickSort(A):
    quickSortBantu(A, 0, len(A) -1 )  # Memanggil quickSortBantu 

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)       # Atur elemen dan dapatkan TitikBelah
        quickSortBantu(A, awal, titikBelah - 1)    # Ini rekursi untuk belah sisi kiri
        quickSortBantu(A, titikBelah + 1, akhir)   # dan belah sisi kanan
    
def partisi(A,awal,akhir):
    nilaiPivot = A[awal]   # Disini nilaiPivot kita ambil dari elemen yang paling kir
    
    penandaKiri = awal + 1  # Posisi awal penandaKiri
    penandaKanan = akhir    # Posisi awal penandaKanan

    selesai = False
    while not selesai:
        
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1
            
        while A[penandaKanan] >= nilaipivot and penandaKanan >= penandaKiri :
            penandaKanan = penandaKanan - 1
            
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp
    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan
    
z = [41,23,21,23,4,5,67,37]
print("z : ",z)
quickSort(z)
print("urutkan z :",z)
