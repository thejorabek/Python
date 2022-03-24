import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

# cursor.execute("CREATE TABLE gta (release_year INTEGER, release_name TEXT, city TEXT)")

release_list = [
	(1997, "Grand Theft Auto", "state of New Guernsey"),
	(1999, "Grand Theft Auto 2", "Anywhere, USA"),
	(2001, "Grand Theft Auto III", "Liberty City"),
	(2002, "Grand Theft Auto: Vice City", "Vice City"),
	(2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
	(2008, "Grand Theft Auto IV", "Liberty City"),
	(2013, "Grand Theft Auto V", "Los Santos"),
]

# cursor.executemany("INSERT INTO gta VALUES (?,?,?)",release_list)

# for i in cursor.execute("SELECT * FROM gta"):
# 	print(i)

cursor.execute("SELECT * FROM gta WHERE city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

connection.close()