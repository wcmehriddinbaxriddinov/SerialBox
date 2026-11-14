# SerialBox

Sevimli seriallarim: Python va SQLite asosidagi konsol dasturi.
Najot Ta'lim o'quv markazidagi yakuniy loyiha.

## Imkoniyatlari

- Serial qo'shish (nomi, janr, yil, reyting)
- Barcha seriallarni jadval ko'rinishida ko'rish
- Nomi, janri yoki yili bo'yicha qidirish
- Reyting bo'yicha saralash (yuqoridan pastga va pastdan yuqoriga)
- Serialni o'chirish
- Serial reytingini yangilash
- Statistika: jami soni, o'rtacha reyting, eng yaxshi serial

## Texnologiyalar

- Python 3
- SQLite3 (Python bilan birga keladi, alohida o'rnatish shart emas)

## Loyiha tuzilishi

```
serialbox/
├── main.py       menu va dasturni ishga tushirish
├── database.py   bazaga ulanish va jadval yaratish
└── funksiya.py   barcha funksiyalar
```

## Ishga tushirish

```
git clone https://github.com/FOYDALANUVCHI_NOMI/serialbox.git
cd serialbox
python main.py
```

Birinchi ishga tushganda `baza.db` fayli avtomatik yaratiladi va 10 ta tayyor serial qo'shiladi.

## Jadval tuzilishi

| Ustun | Turi | Izoh |
|---|---|---|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| nomi | TEXT | Serial nomi |
| janr | TEXT | Janri |
| yil | INTEGER | Chiqqan yili |
| reyting | REAL | 0 dan 10 gacha |
| created_at | TIMESTAMP | Qo'shilgan sana |

## Muallif

Mexriddin