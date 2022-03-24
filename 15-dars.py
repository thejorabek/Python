import sqlite3

connection=sqlite3.connect("Meva.db")
kursor=connection.cursor()
def create_table():
	kursor.execute("CREATE TABLE IF NOT EXISTS fruit(name TEXT, price REAL, type TEXT)")
	connection.commit() #ma'lumotlarni saqlaydi
def insert_info(nomi, narxi, turi):
	kursor.execute("INSERT INTO fruit VALUES(?,?,?)",(nomi, narxi, turi))
	connection.commit()
def selection():
	kursor.execute("SELECT * FROM fruit WHERE price>20000 ORDER BY price DESC")
	kursor.execute("SELECT * FROM fruit")
	st=kursor.fetchall() # Barcha ma'lumotni o'qiydi
	st=kursor.fetchone() # Barcha ma'lumotni o'qiydi
	st=kursor.fetchmany(4) # Berilgan ma'lumotni o'qiydi
	print(st)
	for i in st:
		print(*i)
def delete_info(nomi):
	kursor.execute("DELETE FROM fruit WHERE name=(?) or price>40000",(nomi,))
	connection.commit()
def update_info():
	kursor.execute("UPDATE fruit SET name='Olma' WHERE price<20000")
	connection.commit()
create_table()
for i in range(int(input("Nechta: "))):
	insert_info(input("Name: "),float(input("Price: ")),input("Type: "))
selection()
delete_info(input("Name: "))
update_info()
connection.close()
create_table()
for i in range(int(input("Nechta: "))):
	insert_info(input("Name: "), float())
connection.close()