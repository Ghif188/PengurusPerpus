list_buku = ["Panduan mengaji", "Matematika diskrit", "Algoritma kehidupan"]
list_penulis = ["Hanif", "Farzi", "Kiyawa"]
list_peminjam = []
list_buku_dipinjam = []
list_penulis_buku_dipinjam = []

def memakai():
    print("Pilih Menu:")
    print("klik 1 => Memasukkan Buku Baru")
    print("klik 2 => Cari buku tersedia")
    print("klik 3 => Melihat Daftar Buku Yang Tersedia")
    print("klik 4 => Menghapus Buku Dari Daftar Buku")
    print("klik 5 => Peminjaman Buku")
    print("klik 6 => List Peminjam Buku")
    print("klik 7 => Pengembalian Buku")
    print("")
    kegiatan = input("Masukkan nomor menu: ")
    print("==============================")
    if kegiatan == "1":
        memasukkan_buku_baru()
    elif kegiatan == "2":
        pencarian()
    elif kegiatan == "3":
        melihat_list()
    elif kegiatan == "4":
        menghapus_buku()
    elif kegiatan == "5":
        peminjaman_buku()
    elif kegiatan == "6":
        list_peminjaman_buku()
    elif kegiatan == "7":
        pengembalian_buku()
    else:
        print("Pilihan Menu Tidak ada, Diharapkan untuk memilih dengan benar!")
        memakai()
        
def sorting():
    global list_buku
    global list_penulis
    for i in range(len(list_buku)-1):
        terkecil = i
        for j in range(i+1, len(list_buku)):
            if list_buku[j] < list_buku[terkecil]:
                terkecil = j
        tmp_buku = list_buku[terkecil]
        list_buku[terkecil] = list_buku[i]
        list_buku[i] = tmp_buku
        tmp_penulis = list_penulis[terkecil]
        list_penulis[terkecil] = list_penulis[i]
        list_penulis[i] = tmp_penulis
        
def memasukkan_buku_baru():
    global list_buku
    global list_penulis
    masukkan_nama_buku_inp = input("Masukkan Nama Buku: ").capitalize()
    masukkan_nama_penulis_inp = input("Masukkan Nama Penulis Buku: ").capitalize()
    list_buku.append(masukkan_nama_buku_inp)
    list_penulis.append(masukkan_nama_penulis_inp)
    print("")
    print("- Buku Berhasil Dimasukkan Ke Dalam List Baru -")
    sorting()
    print("==============================")
    memakai_lagi = input("Apakah masih ingin menggunakan aplikasi ? (y/n): ")
    print("==============================")
    print("")
    if memakai_lagi == "y":
        memakai()
    else:
        print("GOODBYE !")
            
def pencarian():
    global list_buku
    global list_penulis
    input_pencarian = input("Masukkan Judul Buku yang Dicari: ")
    hasil_sesuai = []
    hasil_penulis_sesuai = []
    for i in range(len(list_buku)):
        if len(list_buku[i]) >= len(input_pencarian):
            jumlah_huruf_sama = 0
            for j in range(len(input_pencarian)):
                desimal_input = ord(input_pencarian[j])
                desimal_list = ord(list_buku[i][j])
                if desimal_input >= 97 and desimal_input <= 122:
                    desimal_input -= 32
                if desimal_list >= 97 and desimal_list <= 122:
                    desimal_list -= 32
                if desimal_input == desimal_list:
                    jumlah_huruf_sama += 1
            if jumlah_huruf_sama == len(input_pencarian):
                hasil_sesuai.append(list_buku[i]) 
                hasil_penulis_sesuai.append(list_penulis[i])
        else:
            continue   
    print("")
    if len(hasil_sesuai) == 0:
        print("- Tidak Ada Hasil yang Cocok -")
    else:
        for i in range(len(hasil_sesuai)):
            print(str(i+1) + ".", hasil_sesuai[i] + ", Karya", hasil_penulis_sesuai[i])
    print("")
    print("==============================")
    memakai_lagi = input("Apakah kamu ingin melanjutkan ke menu ? (y/n): ")
    print("==============================")
    print("")
    if memakai_lagi == "y":
        memakai()
    else:
        print("GOODBYE !")

def melihat_list():
    global list_buku
    global list_penulis
    sorting()
    print("List Buku yang Tersedia:")
    print("")
    for j in range(len(list_buku)):
        print(str(j+1)+".", list_buku[j] + ", karya", list_penulis[j])
    print("")
    print("==============================")
    memakai_lagi = input("Apakah masih ingin menggunakan aplikasi ? (y/n): ")
    print("==============================")
    print("")
    if memakai_lagi == "y":
        memakai()
    else:
        print("GOODBYE !")

def menghapus_buku():
    global list_buku
    global list_penulis
    masukkan_nama_buku_del = input("Masukkan Nama Buku: ").capitalize()
    masukkan_nama_penulis_del = input("Masukkan Nama Penulis Buku: ").capitalize()
    berhasil = "no"
    for i in range(len(list_buku)):
        if masukkan_nama_buku_del == list_buku[i] and masukkan_nama_penulis_del == list_penulis[i]:
            list_buku.pop(i)
            list_penulis.pop(i)
            berhasil = "yes"
            break
    print("")
    if berhasil == "yes":
        print("- Berhasil Menghapus data -")
        print("==============================")
        memakai_lagi = input("Apakah masih ingin menggunakan aplikasi ? (y/n): ")
        print("==============================")
        print("")
        if memakai_lagi == "y":
            memakai()
        else:
            print("GOODBYE !")
    else:
        print("- Pastikan Buku yang anda masukkan benar! -")
        ulang = input("Ingin memuat ulang form? (y/n): ")
        print("")
        print("==============================")
        if ulang == "y":
            menghapus_buku()
        else:
            memakai()
    
def peminjaman_buku():
    global list_buku
    global list_penulis
    global list_peminjam
    global list_buku_dipinjam
    global list_penulis_buku_dipinjam
    masukkan_nama_peminjam = input("Masukkan Nama Peminjam Buku: ").capitalize()
    masukkan_nama_buku_pinjam = input("Masukkan Nama Buku: ").capitalize()
    masukkan_nama_penulis_pinjam = input("Masukkan Nama Penulis Buku: ").capitalize()
    berhasil = "no"
    for k in range(len(list_buku)):
        if list_buku[k] == masukkan_nama_buku_pinjam and list_penulis[k] == masukkan_nama_penulis_pinjam :
            list_peminjam.append(masukkan_nama_peminjam)
            list_buku_dipinjam.append(list_buku[k])
            list_penulis_buku_dipinjam.append(list_penulis[k]) 
            list_buku.pop(k)
            list_penulis.pop(k)
            berhasil = "yes"
            break
    print("")
    if berhasil == "yes":
        print("- Berhasil meminjam buku -")
        print("==============================")
        memakai_lagi = input("Apakah masih ingin menggunakan aplikasi ? (y/n): ")
        print("==============================")
        print("")
        if memakai_lagi == "y":
            memakai()
        else:
            print("GOODBYE !")
    else:
        print("- Pastikan buku serta penulisnya benar dan tersedia! -")
        ulang = input("Ingin memuat ulang form? (y/n): ")
        print("")
        print("==============================")
        if ulang == "y":
            peminjaman_buku()
        else:
            print("")
            memakai()
        
def list_peminjaman_buku():
    global list_peminjam
    global list_buku_dipinjam
    global list_penulis_buku_dipinjam
    print("List Peminjam Buku:")
    if len(list_peminjam) == 0:
        print("")
        print("- Tidak Ada Peminjam -")
    for l in range(len(list_peminjam)):
        print(str(l+1)+".", "Peminjam:", list_peminjam[l] + ", Buku:", list_buku_dipinjam[l] + ", Karya:", list_penulis_buku_dipinjam[l])
    print("")
    print("==============================")
    memakai_lagi = input("Apakah kamu ingin melanjutkan ke menu ? (y/n): ")
    print("==============================")
    print("")
    if memakai_lagi == "y":
        memakai()
    else:
        print("GOODBYE !")

def pengembalian_buku():
    global list_buku
    global list_penulis
    global list_peminjam
    global list_buku_dipinjam
    global list_penulis_buku_dipinjam
    masukkan_nama_peminjam = input("Masukkan Nama Peminjam Buku: ").capitalize()
    masukkan_nama_buku_pinjam = input("Masukkan Nama Buku: ").capitalize()
    masukkan_nama_penulis_pinjam = input("Masukkan Nama Penulis Buku: ").capitalize()
    berhasil = "no"
    for m in range(len(list_buku_dipinjam)):
        if masukkan_nama_buku_pinjam == list_buku_dipinjam[m] and masukkan_nama_penulis_pinjam == list_penulis_buku_dipinjam[m] and masukkan_nama_peminjam == list_peminjam[m]:
            list_buku.append(list_buku_dipinjam[m])
            list_penulis.append(list_penulis_buku_dipinjam[m])
            list_buku_dipinjam.pop(m)
            list_penulis_buku_dipinjam.pop(m)
            list_peminjam.pop(m)
            berhasil = "yes"
            break
        else:
            continue
    print("")
    if berhasil == "yes":
        print("- Berhasil mengembalikan buku, Terimakasih -")
        print("==============================")
        memakai_lagi = input("Apakah kamu ingin melanjutkan ke menu ? (y/n): ")
        print("==============================")
        print("")
        if memakai_lagi == "y":
            memakai()
        else:
            print("GOODBYE !")
    else:
        print("- Pastikan data yang anda masukkan benar! -")
        ulang = input("Ingin memuat ulang form? (y/n): ")
        if ulang == "y":
            print("")
            print("==============================")
            pengembalian_buku()
        else:
            memakai()

print("=====================")
print("PENGURUS PERPUSTAKAAN")
print("=====================")
sorting()
memakai()