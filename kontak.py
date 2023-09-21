# Program Kontak
# List Kontak
namaKontak = ['Naufal', 'Hazim']
noTelepon = ['08123456789', '08987654321']


def daftarKontak():  # fungsi untuk menampilkan kontak yang tersimpan di list kontak
    print('Daftar Kontak:')
    for i in range(len(namaKontak)):
        print('Nama: {}'.format(namaKontak[i]))
        print('No Telepon: {}'.format(noTelepon[i]))


def tambahKontak():  # fungsi untuk menambahkan kontak
    namaKontak.append(input('Nama: '))
    noTelepon.append(input('No Telepon: '))
    print('Kontak berhasil ditambahkan')


print('Selamat datang!')
while True:
    print('---Menu---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    menu = int(input('Pilih Menu: '))
    if menu == 1:
        daftarKontak()
    elif menu == 2:
        tambahKontak()
    elif menu == 3:
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia')
