#membuat table
import sqlite3
koneksi = sqlite3.connect('HewanLangka.db') 

koneksi.execute('''
                CREATE TABLE HEWAN(
                id_hewan INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_hewan VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_sekarang INTEGER(10),
                thn_ditemukan INTEGER(10)
                )
                ''')

koneksi.close()