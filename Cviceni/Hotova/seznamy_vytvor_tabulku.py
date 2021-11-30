def vytvor_tabulku(velikost = 11):
    seznam_radku = []
    for a in range(velikost):
        radek = []
        for b in range(velikost):
            radek.append(a * b)
        seznam_radku.append(radek)
    return seznam_radku

nasobilka = vytvor_tabulku()

# Vypíše:
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 
# 50], [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60], [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70], [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80], [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]

# Vypíše výsledek násobení:
print(nasobilka[2][3])  # dva krát tři
print(nasobilka[5][2])  # pět krát dva
print(nasobilka[8][7])  # osm krát sedm

# Vypsání celé tabulky
for radek in nasobilka:
    for cislo in radek:
        print(cislo, end= ' ')
    print()
    
# Vypíše:
# 0 0 0 0 0 0 0 0 0 0 0
# 0 1 2 3 4 5 6 7 8 9 10
# 0 2 4 6 8 10 12 14 16 18 20
# 0 3 6 9 12 15 18 21 24 27 30
# 0 4 8 12 16 20 24 28 32 36 40
# 0 5 10 15 20 25 30 35 40 45 50
# 0 6 12 18 24 30 36 42 48 54 60
# 0 7 14 21 28 35 42 49 56 63 70 
# 0 8 16 24 32 40 48 56 64 72 80
# 0 9 18 27 36 45 54 63 72 81 90
# 0 10 20 30 40 50 60 70 80 90 100
