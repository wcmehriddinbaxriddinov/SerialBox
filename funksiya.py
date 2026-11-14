from database import ulanish


def jadval_chiqar(natija):
    if not natija:
        print("Ma'lumot topilmadi.")
        return
    print(f"\n{'ID':<5}{'Nomi':<22}{'Janr':<14}{'Yil':<7}{'Reyting':<9}{'Sana'}")
    print("-" * 75)
    for q in natija:
        print(f"{q[0]:<5}{q[1]:<22}{q[2]:<14}{q[3]:<7}{q[4]:<9}{q[5]}")


def qoshish():
    nomi = input("Serial nomi: ")
    janr = input("Janr: ")
    yil = int(input("Yil: "))
    reyting = float(input("Reyting (0-10): "))

    db = ulanish()
    kursor = db.cursor()
    kursor.execute(
        "INSERT INTO seriallar (nomi, janr, yil, reyting) VALUES (?, ?, ?, ?)",
        (nomi, janr, yil, reyting)
    )
    db.commit()
    db.close()
    print(f"{nomi} saqlandi!")


def korish():
    db = ulanish()
    kursor = db.cursor()
    kursor.execute("SELECT id, nomi, janr, yil, reyting, created_at FROM seriallar")
    natija = kursor.fetchall()
    db.close()
    jadval_chiqar(natija)


def qidirish():
    print("1. Nomi bo'yicha")
    print("2. Janr bo'yicha")
    print("3. Yil bo'yicha")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        ustun = "nomi"
    elif tanlov == "2":
        ustun = "janr"
    elif tanlov == "3":
        ustun = "yil"
    else:
        print("Noto'g'ri tanlov!")
        return

    soz = input("Qidiruv so'zi: ")

    db = ulanish()
    kursor = db.cursor()
    kursor.execute(
        f"SELECT id, nomi, janr, yil, reyting, created_at FROM seriallar WHERE {ustun} LIKE ?",
        (f"%{soz}%",)
    )
    natija = kursor.fetchall()
    db.close()
    jadval_chiqar(natija)


def saralash():
    print("1. Reyting yuqoridan pastga")
    print("2. Reyting pastdan yuqoriga")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        tartib = "DESC"
    elif tanlov == "2":
        tartib = "ASC"
    else:
        print("Noto'g'ri tanlov!")
        return

    db = ulanish()
    kursor = db.cursor()
    kursor.execute(
        f"SELECT id, nomi, janr, yil, reyting, created_at FROM seriallar ORDER BY reyting {tartib}"
    )
    natija = kursor.fetchall()
    db.close()
    jadval_chiqar(natija)


def ochirish():
    korish()
    serial_id = int(input("\nO'chiriladigan serial ID si: "))

    db = ulanish()
    kursor = db.cursor()
    kursor.execute("SELECT nomi FROM seriallar WHERE id = ?", (serial_id,))
    serial = kursor.fetchone()

    if serial is None:
        print("Bunday ID topilmadi!")
        db.close()
        return

    kursor.execute("DELETE FROM seriallar WHERE id = ?", (serial_id,))
    db.commit()
    db.close()
    print(f"{serial[0]} o'chirildi.")


def reyting_yangilash():
    korish()
    serial_id = int(input("\nReytingi o'zgaradigan serial ID si: "))
    yangi = float(input("Yangi reyting (0-10): "))

    db = ulanish()
    kursor = db.cursor()
    kursor.execute("SELECT nomi FROM seriallar WHERE id = ?", (serial_id,))
    serial = kursor.fetchone()

    if serial is None:
        print("Bunday ID topilmadi!")
        db.close()
        return

    kursor.execute("UPDATE seriallar SET reyting = ? WHERE id = ?", (yangi, serial_id))
    db.commit()
    db.close()
    print(f"{serial[0]} reytingi {yangi} ga o'zgartirildi.")


def statistika():
    db = ulanish()
    kursor = db.cursor()
    kursor.execute("SELECT COUNT(*), AVG(reyting) FROM seriallar")
    jami, ortacha = kursor.fetchone()

    if jami == 0:
        print("Ma'lumot yo'q.")
        db.close()
        return

    kursor.execute("SELECT nomi, reyting FROM seriallar ORDER BY reyting DESC LIMIT 1")
    eng_yaxshi = kursor.fetchone()
    db.close()

    print("\n======== Statistika ========")
    print(f"Jami seriallar: {jami} ta")
    print(f"O'rtacha reyting: {ortacha:.2f}")
    print(f"Eng yaxshi serial: {eng_yaxshi[0]} ({eng_yaxshi[1]})")