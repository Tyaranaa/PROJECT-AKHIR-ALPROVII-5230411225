
import sqlite3

koneksi = sqlite3.connect('HewanLangka.db')
kursor = koneksi.cursor()

jenis = 'Mamalia'
kursor.execute(f"DELETE FROM HEWAN WHERE jenis = 'Mamalia'")
koneksi.commit()


if kursor.rowcount > 0:
    print(f"Data hewan dengan jenis {jenis} berhasil di update.")
else:
    print(f"Tidak ada data hewan dengan jenis {jenis}.")
    

koneksi.close()
    