import sqlite3

boglan = sqlite3.connect("customer.db")

kursor = boglan.cursor()

kursor.execute("""CREATE TABLE IF NOT EXISTS customer (
				  first_name TEXT,
				  last_name TEXT,
				  email TEXT
	)""")

boglan.commit()

boglan.close()