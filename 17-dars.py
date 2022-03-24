import sqlite3

class DataBase():
    def __init__(self):
        self.con=sqlite3.connect("MARKAZ.db")
        self.k=self.con.cursor()
        self.create()
        # self.insert()
        self.inner_join()
        self.left_join()
        self.right_join()
        self.full_outer_join()
        self.cross_join()
        self.con.close()
    def create(self):
        self.k.execute('''CREATE TABLE IF NOT EXISTS Kurs
                      (Kurs_id NUMERIC, 
                       Kurs_name TEXT, 
                       PRIMARY KEY(Kurs_id))''')
        self.k.execute('''CREATE TABLE IF NOT EXISTS talaba
                      (talaba_id NUMERIC,
                       talaba_name TEXT,
                       kurs_id NUMERIC,
                       FOREIGN KEY(kurs_id) 
                       REFERENCES Kurs(Kurs_id),
                       PRIMARY KEY(talaba_id))''')
        self.con.commit()
    def insert(self):
        self.k.execute('''INSERT INTO Kurs 
                          VALUES
                           (1,'FrontEnd'),
                           (2,'NodeJS'),
                           (3,'.NET'),
                           (4,'Java(Spring)'),
                           (5,'GOLANG'),
                           (6,'FLUTTER')''')
        self.k.execute('''INSERT INTO talaba 
                          VALUES
                           (1,'Abdurahmon',5),
                           (2,'Soburjon',4),
                           (3,'Ibrohim',2),
                           (4,'MuhammadYusuf',5),
                           (5,'Akbarshox',1),
                           (6,'Shaxboz',3),
                           (7,'Rovshan',4),
                           (8,'Abrorxon',3),
                           (9,'Pulat',1),
                           (10,"Jo'rabek",2),
                           (11,'Sherzod',7),
                           (12,'Toxir',1),
                           (13,'Temur',5),
                           (14,'Saidkabr',7)''')
        self.con.commit()
    def inner_join(self):
        print("============INNER============")
        self.k.execute('''SELECT talaba_id, talaba_name, Kurs_name 
                          FROM talaba
                          INNER JOIN Kurs
                          ON talaba.kurs_id=Kurs.Kurs_id''')
        for i in self.k.fetchall():
            print(*i)
    def left_join(self):
        print("============LEFT============")
        self.k.execute('''SELECT talaba_id, talaba_name, Kurs_name 
                          FROM talaba
                          LEFT JOIN Kurs
                          USING(Kurs_id)''')
        for i in self.k.fetchall():
            print(*i)
    def right_join(self):
        print("============RIGHT============")
        self.k.execute('''SELECT talaba_id, talaba_name, Kurs_name 
                          FROM Kurs
                          LEFT JOIN talaba
                          USING(Kurs_id)''')
        for i in self.k.fetchall():
            print(*i)
    def full_outer_join(self):
        print("============FULL OUTTER============")
        self.k.execute('''SELECT talaba_id, talaba_name, Kurs_name 
                          FROM talaba
                          LEFT JOIN Kurs
                          USING(Kurs_id)
                          UNION ALL
                          SELECT talaba_id, talaba_name, Kurs_name 
                          FROM Kurs
                          LEFT JOIN talaba
                          USING(Kurs_id)''')
        for i in self.k.fetchall():
            print(*i)
    def cross_join(self):
        print("============CROSS============")
        self.k.execute('''SELECT talaba_id, talaba_name, Kurs_name 
                          FROM Kurs
                          CROSS JOIN talaba 
                          ORDER BY Kurs_name''')
        for i in self.k.fetchall():
            print(*i)

obj=DataBase()