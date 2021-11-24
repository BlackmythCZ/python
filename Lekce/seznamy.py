cisla = [1, 1, 2, 3, 5, 8, 13]
print(cisla)

for cislo in cisla:
    print(cislo)

seznam = [1, 'abc', True, None, range(10), len]
print(seznam)

print(cisla[2])

print(cisla[2:-3])

# Důležitá vlastnost seznamů, kterou nemají ani čísla, ani řetězce (a True/False/None už vůbec ne), je, že seznamy se dají měnit.
prvocisla = [2, 3, 5, 7, 11, 13, 17]
print(prvocisla)
prvocisla.append(19)
print(prvocisla)

a = [1, 2, 3] # vytvoření seznamu
b = a # tady se nový seznam nevytváří

# seznam vytvořený v prvním řádku má teď dvě jména: "a" a "b",
# ale stále pracujeme jenom s jedním seznamem

print(b)
a.append(4)
print(b)
print(a)

# Kromě metody append, která přidává jediný prvek, existuje metoda extend, která umí přidávat prvků víc. Prvky k přidání jí předáme ve formě seznamu:
dalsi_prvocisla = [23, 29, 31]
prvocisla.extend(dalsi_prvocisla)
print(prvocisla)


