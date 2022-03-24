# import sqlite3

# boglanish = sqlite3.connect("talaba.db")

# kursor = boglanish.cursor()

# # def table_kirit():
# # 	kursor.execute("CREATE TABLE IF NOT EXISTS jadval (id INTEGER, ism TEXT, yosh INTEGER)")
# # 	boglanish.commit()

# # def insert_info(idsi, ismi, yoshi):
# # 	kursor.execute("INSERT INTO jadval VALUES(?,?,?)",(idsi, ismi, yoshi))
# # 	boglanish.commit()
# # for i in range(int(input("Nechta: "))):
# # 	insert_info(input("id: "),input("ism: "),input("yosh: "))

# # def update():
# # 	kursor.execute("UPDATE jadval SET id='1' WHERE id='2'")
# # 	kursor.execute("UPDATE jadval SET id='3' WHERE id='4'")
# # 	kursor.execute("UPDATE jadval SET id='5' WHERE id='6'")
# # 	boglanish.commit()

# def query():
# 	kursor.execute("SELECT * FROM jadval WHERE id%2!=0")
# 	st=kursor.fetchall()
# 	for i in st:
# 		print(*i)

# # table_kirit()
# # insert_info()
# # update()
# query()
# boglanish.close() 



import sqlite3

boglanish = sqlite3.connect("Talaba.db")

kursor = boglanish.cursor()

# def table_kirit():
# 	kursor.execute("CREATE TABLE IF NOT EXISTS jadval (id INTEGER, ism TEXT, yosh INTEGER, baho INTEGER)")
# 	boglanish.commit()

# def insert_info(idsi, ismi, yoshi, bahosi):
# 	kursor.execute("INSERT INTO jadval VALUES(?,?,?,?)",(idsi, ismi, yoshi, bahosi))
# 	boglanish.commit()
# for i in range(int(input("Nechta: "))):
# 	insert_info(input("id: "),input("ism: "),input("yosh: "),input("bahosi: "))

# def alo_info():
# 	kursor.execute("SELECT * FROM jadval WHERE baho>=90 AND baho<=100 ORDER BY ism ASC")
# 	st=kursor.fetchall()
# 	for i in st:
# 		print(*i)

# def yaxshi_info():
# 	kursor.execute("SELECT * FROM jadval WHERE baho>=70 AND baho<=90 ORDER BY yosh DESC")
# 	st=kursor.fetchall()
# 	for i in st:
# 		print(*i)

def qoniqarli_info():
	kursor.execute("SELECT * FROM jadval WHERE baho>=60 AND baho<=70 ORDER BY baho ASC")
	st=kursor.fetchall()
	for i in st:
		print(*i)

# table_kirit()
# insert_info()
# alo_info()
# yaxshi_info()
qoniqarli_info()
boglanish.close()