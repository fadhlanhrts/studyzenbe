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
c.execute("DROP TABLE mycourse")
c.execute("DROP TABLE harienum")
c.execute("DROP TABLE pertemuan")
c.execute("DROP TABLE course")
'''
c.execute("CREATE TABLE harienum(id INTEGER PRIMARY KEY AUTOINCREMENT, hari TEXT)")
c.execute("CREATE TABLE pertemuan(id INTEGER PRIMARY KEY AUTOINCREMENT, hari REFERENCES harienum(id), jam_start TEXT, jam_end TEXT)")
c.execute("CREATE TABLE course(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, sks INTEGER, term INTEGER, pertemuan_id REFERENCES pertemuan(id))")
c.execute("CREATE TABLE mycourse(id INTEGER PRIMARY KEY AUTOINCREMENT, course_id REFERENCES course(id))")
c.execute("INSERT INTO harienum(hari) VALUES ('SENIN'), ('SELASA'), ('RABU'), ('KAMIS'), ('JUMAT'), ('SABTU'), ('MINGGU')")
c.execute("INSERT INTO pertemuan(hari, jam_start, jam_end) VALUES (1, '2021-10-13 08:00:00.000', '2021-10-13 09:40:00.000'), (1, '2021-10-13 10:00:00.000', '2021-10-13 11:40:00.000'),(1, '2021-10-13 13:00:00.000', '2021-10-13 14:40:00.000'), (1, '2021-10-13 16:00:00.000', '2021-10-13 17:40:00.000'), (1, '2021-10-13 08:00:00.000', '2021-10-13 10:30:00.000'), (1, '2021-10-13 10:00:00.000', '2021-10-13 12:30:00.000'),(1, '2021-10-13 13:00:00.000', '2021-10-13 15:30:00.000'), (1, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000'), (2, '2021-10-13 08:00:00.000', '2021-10-13 09:40:00.000'), (2, '2021-10-13 10:00:00.000', '2021-10-13 11:40:00.000'),(2, '2021-10-13 13:00:00.000', '2021-10-13 14:40:00.000'), (2, '2021-10-13 16:00:00.000', '2021-10-13 17:40:00.000'), (2, '2021-10-13 08:00:00.000', '2021-10-13 10:30:00.000'), (2, '2021-10-13 10:00:00.000', '2021-10-13 12:30:00.000'),(2, '2021-10-13 13:00:00.000', '2021-10-13 15:30:00.000'), (2, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000'), (3, '2021-10-13 08:00:00.000', '2021-10-13 09:40:00.000'), (3, '2021-10-13 10:00:00.000', '2021-10-13 11:40:00.000'),(3, '2021-10-13 13:00:00.000', '2021-10-13 14:40:00.000'), (3, '2021-10-13 16:00:00.000', '2021-10-13 17:40:00.000'), (3, '2021-10-13 08:00:00.000', '2021-10-13 10:30:00.000'), (3, '2021-10-13 10:00:00.000', '2021-10-13 12:30:00.000'),(3, '2021-10-13 13:00:00.000', '2021-10-13 15:30:00.000'), (3, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000'), (4, '2021-10-13 08:00:00.000', '2021-10-13 09:40:00.000'), (4, '2021-10-13 10:00:00.000', '2021-10-13 11:40:00.000'),(4, '2021-10-13 13:00:00.000', '2021-10-13 14:40:00.000'), (4, '2021-10-13 16:00:00.000', '2021-10-13 17:40:00.000'), (4, '2021-10-13 08:00:00.000', '2021-10-13 10:30:00.000'), (4, '2021-10-13 10:00:00.000', '2021-10-13 12:30:00.000'),(4, '2021-10-13 13:00:00.000', '2021-10-13 15:30:00.000'), (4, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000'), (5, '2021-10-13 08:00:00.000', '2021-10-13 09:40:00.000'), (5, '2021-10-13 10:00:00.000', '2021-10-13 11:40:00.000'),(5, '2021-10-13 13:00:00.000', '2021-10-13 14:40:00.000'), (5, '2021-10-13 16:00:00.000', '2021-10-13 17:40:00.000'), (5, '2021-10-13 08:00:00.000', '2021-10-13 10:30:00.000'), (5, '2021-10-13 10:00:00.000', '2021-10-13 12:30:00.000'),(5, '2021-10-13 13:00:00.000', '2021-10-13 15:30:00.000'), (5, '2021-10-13 16:00:00.000', '2021-10-13 18:30:00.000')")
c.execute("INSERT INTO course(name, sks, term, pertemuan_id) VALUES ('Despro', 3, 7, 40),('Sistem Waktu Nyata dan IoT', 3, 5, 32),('Teknologi Big Data', 3, 7 , 8),('Jaringan Komputer Selasa', 2, 5, 9),('Jaringan Komputer Kamis', 2, 5, 25),('Dasar Sitem Digital',3, 1, 38),('Jaringan Telekomunikasi',3, 5, 13),('Object Oriented Programming',3, 3, 23),('Probstok',2, 5, 12),('RPL',3, 5, 7),('Statistika',3, 3, 37),('Diskrit',3, 3, 26),('Sinsis',2, 5, 25),('Rangkaian Listrik',2, 3, 11)")


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
