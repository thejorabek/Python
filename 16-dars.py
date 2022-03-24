import sqlite3

class Menu():
	def __init__(self):
		self.boglan=sqlite3.connect("Milliy_taomlar.db")
		self.kursor=self.boglan.cursor()
		self.create()
		self.sorov()
		self.boglan.close()

	def create(self):
			self.kursor.execute("CREATE TABLE IF NOT EXISTS ovqat (id INTEGER, taom_nomi TEXT, taom_masalliqlari TEXT)")
			self.boglan.commit()
	def sorov(self):
		print("=====1-SO'ROV=====")
		self.kursor.execute("SELECT * FROM ovqat WHERE taom_nomi LIKE '%a'")
		for i in self.kursor.fetchall():
			print(*i)

		print("=====2-SO'ROV=====")
		self.kursor.execute("SELECT * FROM ovqat WHERE taom_masalliqlari LIKE '%guruch%'")
		for i in self.kursor.fetchall():
			print(*i)

obj=Menu()


# import sqlite3

# class Menu():
# 	def __init__(self):
# 		self.boglan=sqlite3.connect("Bozor.db")
# 		self.kursor=self.boglan.cursor()
# 		self.create()
# 		self.sorov()
# 		self.boglan.close()

# 	def create(self):
# 			self.kursor.execute("CREATE TABLE IF NOT EXISTS meva (id INTEGER, meva_nomi TEXT, meva_narxi INTEGER, meva_turi TEXT)")
# 			self.boglan.commit()
# 	def sorov(self):
# 		print("=====1-SO'ROV=====")
# 		self.kursor.execute("SELECT * FROM meva WHERE meva_turi LIKE ''")
# 		for i in self.kursor.fetchall():
# 			print(*i)

# 		print("=====2-SO'ROV=====")
# 		self.kursor.execute("SELECT * FROM meva WHERE taom_nomi LIKE '%a'")
# 		for i in self.kursor.fetchall():
# 			print(*i)
# 		pass

# obj=Menu()