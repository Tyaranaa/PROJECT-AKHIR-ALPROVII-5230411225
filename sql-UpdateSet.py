
import sqlite3
koneksi = sqlite3.connect('HewanLangka.db')
kursor = koneksi.cursor()

id_hewan = 1
jumlah_baru = 900

kursor.execute(f'''
               UPDATE HEWAN SET jml_sekarang = '900' WHERE id_hewan = '1'
                ''')
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil di update.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")
    

koneksi.close()
    