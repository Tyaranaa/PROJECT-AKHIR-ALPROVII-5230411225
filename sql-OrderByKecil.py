
import sqlite3
koneksi = sqlite3.connect('HewanLangka.db')
kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY jml_sekarang SDESC")
baris_table = kursor.fetchall()

print("SELECT WHERE AND: Mamalia dan Asal")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*100)

for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))
print("-"*100)

koneksi.close()