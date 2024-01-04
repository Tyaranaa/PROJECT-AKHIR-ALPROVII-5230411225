

import sqlite3
koneksi = sqlite3.connect('HewanLangka.db')
kursor = koneksi.cursor()

id_hewan = 3
asal = 'Nusa Tenggara Timur'

kursor.execute(f"UPDATE HEWAN SET asal = 'Nusa Tenggara Timur' WHERE id_hewan = {id_hewan}")
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil di update.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")
    

koneksi.close()
    