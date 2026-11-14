import sqlite3


def ulanish():
    return sqlite3.connect("baza.db")


def jadval_yarat():
    db = ulanish()
    kursor = db.cursor()
    kursor.execute(
        "CREATE TABLE IF NOT EXISTS seriallar ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nomi TEXT NOT NULL, "
        "janr TEXT NOT NULL, "
        "yil INTEGER, "
        "reyting REAL, "
        "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    )
    kursor.execute("SELECT COUNT(*) FROM seriallar")
    if kursor.fetchone()[0] == 0:
        malumotlar = [
            ("Breaking Bad", "Drama", 2008, 9.5),
            ("Game of Thrones", "Fantasy", 2011, 9.2),
            ("Peaky Blinders", "Drama", 2013, 8.8),
            ("Stranger Things", "Fantastika", 2016, 8.7),
            ("The Witcher", "Fantasy", 2019, 8.0),
            ("Money Heist", "Triller", 2017, 8.2),
            ("Dark", "Fantastika", 2017, 8.7),
            ("Sherlock", "Detektiv", 2010, 9.1),
            ("Friends", "Komediya", 1994, 8.9),
            ("Squid Game", "Triller", 2021, 8.0)
        ]
        kursor.executemany(
            "INSERT INTO seriallar (nomi, janr, yil, reyting) VALUES (?, ?, ?, ?)",
            malumotlar
        )
    db.commit()
    db.close()