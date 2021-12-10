import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

'''cur.execute("INSERT INTO Livre (firstname, lastname) VALUES (?,?)",
            ('Jean-Claude','IPOULE')
            )

cur.execute("INSERT INTO Etudiant (firstname, lastname) VALUES (?,?)",
            ('Bruno','Bossadé')
            )

cur.execute("INSERT INTO Etudiant (firstname, lastname) VALUES (?,?)",
            ('Salima','Essahli')'''

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Initiation au Machine Learning','20/12/2020','20$','https://mrmint.fr/wp-content/uploads/2017/03/Data-science-octo-300x300.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Les bases de données NoSQL et le Big Data','10/11/2019','22$','https://servimg.eyrolles.com/static/media/1559/9782212141559_internet_h1400.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Data Science avec Python pour les nuls','16/11/2021','26$','https://images.epagine.fr/461/9782412053461_1_75.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Hadoop par la pratique','30/12/2018','16$','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHHCg5Pis6m8o1m2Vu63OojYoD9radq9z2ZA&usqp=CAU')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Initiation au Machine Learning','20/12/2020','29$','https://mrmint.fr/wp-content/uploads/2017/03/Data-science-octo-300x300.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Apache Spark, Developpez en Pyhton pour le Big Data','20/09/2020','30$','https://www.prologue.ca/DATA/LIVRE/grande/9782409033780.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Analyse prédictive Delen Dursun','23/04/2020','27$','https://images.lavoisier.net/couvertures/1317672459.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Python pour la Data Science avec Numpy, Pandas, Matplotlib et Seaborn','20/12/2020','20$','https://mrmint.fr/wp-content/uploads/2017/03/Data-science-octo-300x300.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Data, Engineering and application','06/12/2019','35$','https://images.lavoisier.net/couvertures/1317596933.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Data Science strategy','01/08/2021','34$','https://images.lavoisier.net/couvertures/1317185952.jpg')
            )

cur.execute("INSERT INTO Livre (titre, date_parution, prix, lien_image) VALUES (?,?,?,?)",
            ('Introduction au Deep Learning','1/12/2021','40$','https://images-na.ssl-images-amazon.com/images/I/419L2K0TYIL._SX350_BO1,204,203,200_.jpg')
            )

connection.commit()
connection.close()