import sqlite3
koneksi = sqlite3.connect('HewanLangka.db')
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM HEWAN")
rows = kursor.fetchall()

print("Data Hewan")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("="*100)
for rows in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]))
    
koneksi.close()