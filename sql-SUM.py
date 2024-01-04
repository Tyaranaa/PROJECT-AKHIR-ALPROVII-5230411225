
import sqlite3
koneksi = sqlite3.connect('HewanLangka.db')
kursor = koneksi.cursor()

kursor.execute("SELECT AVG (jml_sekarang) FROM HEWAN")

jml_saatini = kursor.fetchone()[0]

print(f"JUMLAH SAAT INI: {jml_saatini}")
kursor.close()