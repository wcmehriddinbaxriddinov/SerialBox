from database import jadval_yarat
from funksiya import qoshish, korish, qidirish, saralash,ochirish, reyting_yangilash, statistika


def menu():
    jadval_yarat()
    while True:
        print("""
╔════════════ MENU ════════════╗
║     1. Ma'lumot qo'shish     ║
║   2. Ma'lumotlarni ko'rish   ║
║     3. Ma'lumot qidirish     ║
║ 4. Reyting bo'yicha saralash ║
║     5. Serialni o'chirish    ║
║    6. Reytingni yangilash    ║
║        7. Statistika         ║
║         0. Chiqish           ║
╚══════════════════════════════╝""")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            qoshish()
        elif tanlov == "2":
            korish()
        elif tanlov == "3":
            qidirish()
        elif tanlov == "4":
            saralash()
        elif tanlov == "5":
            ochirish()
        elif tanlov == "6":
            reyting_yangilash()
        elif tanlov == "7":
            statistika()
        elif tanlov == "0":
            print("Dastur yakunlandi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov!")


menu()