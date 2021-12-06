# Buat troubleshoot & debugging database 

import sqlite3 

# tabel 
# course - daftar matkul 
# harienum - enum untuk hari
# pertemuan - jadwal course
# mycourse - matkul yang diambil 
#connect to database and create database
conn = sqlite3.connect('course.db')

#membuat cursor untuk membuat query
c = conn.cursor()
'''
c.execute("CREATE TABLE course(id INTEGER PRIMARY KEY, name TEXT, sks INTEGER, term INTEGER)")
c.execute("CREATE TABLE harienum(id INTEGER PRIMARY KEY AUTOINCREMENT, hari TEXT)")
c.execute("INSERT INTO harienum(hari) VALUES ('SENIN'), ('SELASA'), ('RABU'), ('KAMIS'), ('JUMAT'), ('SABTU'), ('MINGGU')")
c.execute("CREATE TABLE pertemuan(id INTEGER PRIMARY KEY, course_id REFERENCES course(id), hari REFERENCES harienum(id), jam_start TEXT, jam_end TEXT)")
c.execute("INSERT INTO course VALUES(1, 'Despro', 3, 7), (2, 'Sistem Waktu Nyata dan IoT', 3, 5), (3, 'Teknologi Big Data', 3, 7), (4, 'Jaringan Komputer', 4, 3), (5, 'Keamanan Jaringan', 3, 5)")
c.execute("INSERT INTO pertemuan VALUES(1, 1, 5, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000'), (2, 2, 4, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000'), (3, 3, 1, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000'), (4, 4, 2, '2021-10-13 08:00:00.000', '2021-10-13 09:40:00.000'), (5, 4, 4, '2021-10-13 08:00:00.000', '2021-10-13 09:40:00.000'),(6, 5, 3, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000')")
c.execute("CREATE TABLE mycourse(id INTEGER PRIMARY KEY AUTOINCREMENT, course_id REFERENCES course(id))")
'''

c.execute("SELECT * FROM pertemuan")
#c.execute("DROP TABLE mycourse")
tes = c.fetchall()


for isi in tes:
    print(isi)
    



print("Command executed successfully...")
#execute cursor command
conn.commit()

#close connection
conn.close()
