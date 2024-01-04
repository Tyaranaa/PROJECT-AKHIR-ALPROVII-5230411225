import sqlite3
koneksi = sqlite3.connect('HewanLangka.db')
kursor = koneksi.cursor()


nama_hewan ='B%'
kursor.execute(f"SELECT * FROM HEWAN WHERE nama_hewan LIKE?", (nama_hewan,))
baris_table = kursor.fetchall()

print("Mencari data hewan")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*100)

for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))
print("-"*100)

koneksi.close()