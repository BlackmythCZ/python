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

# Metoda extend umí pracovat i s jinými typy než se seznamy – ráda zpracuje cokoli, přes co umí cyklit for: např. jednotlivé znaky řetězců, řádky souborů, nebo čísla z range().
seznam = []
seznam.extend('abcdef')
seznam.extend(range(10))
print(seznam)

# Seznamům se dají i měnit jednotlivé prvky a to jednoduše tak, že do prvku přiřadíme, jako by to byla proměnná:
cisla = [1, 0, 3, 4]
cisla[1] = 2
print(cisla)

# řiřazovat se dá i do podseznamu – v tomto případě se podseznam nahradí jednotlivými prvky z toho, co přiřazujeme. Jako u extend můžeš do podseznamu opět přiřadit cokoli, co umí zpracovat for – seznam, řetězec, range() apod.
cisla = [1, 2, 3, 4]
cisla[1:-1] = [6, 5]
print(cisla)

# Přiřazením do podseznamu se dá i změnit délka seznamu, nebo některé prvky úplně odstranit:
cisla = [1, 2, 3, 4]
cisla[1:-1] = [0, 0, 0, 0, 0]
print(cisla)
cisla[1:-1] = []
print(cisla)

# Tenhle výše uvedený zápis pro mazání prvků je ale docela nepřehledný, a proto na to máme zvláštní příkaz jménem del:
cisla = [1, 2, 3, 4, 5, 6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)
del cisla # Maže i proměnné!
#print(cisla)

# Další mazací metody jsou:
# pop, která odstraní a vrátí poslední prvek v seznamu – například pokud mám seznam karet v balíčku, jde takhle jednoduše „líznout” kartu,
# remove, která najde v seznamu daný prvek a odstraní ho,
# clear, která vyprázdní celý seznam.
cisla = [1, 2, 3, 'abc', 4, 5, 6, 12]
posledni = cisla.pop()
print(posledni)
print(cisla)

cisla.remove('abc')
print(cisla)

cisla.clear()
print(cisla)

# A taky tu máme metodu sort, která prvky seznamu seřadí.
seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort()
print(seznam)

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort(reverse=True) # sestupně
print(seznam)

# Spousta toho, co můžeme dělat s řetězci, má stejný účinek i u seznamů. Třeba sečítání a násobení číslem:
melodie = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(melodie)

# Další staří známí jsou funkce len, metody count a index, a operátor in.
print(len(melodie))
print(melodie.count('D'))
print(melodie.index('D')) # Číslo prvního 'D'
print('D' in melodie) # Je 'D' v seznamu?

# Poslední tři se ale přece jen chovají kapku jinak: u řetězců pracují s podřetězci, u seznamů jen s jednotlivými prvky. Takže ačkoliv naše melodie obsahuje prvky 'D' a 'E' vedle sebe, 'DE' v seznamu není:
print(melodie.count('DE'))
#print(melodie.index('DE'))
print('DE' in melodie)

# Seznam se dá použít v příkazu if (nebo while) jako podmínka, která platí, když v tom seznamu něco je. Jinými slovy, seznam je tu „zkratka“ pro len(seznam) > 0.
# Podobně se dají v podmínce použít i řetězce. A dokonce i čísla – ta jako podmínka platí, pokud jsou nenulová.
if seznam:
    print('V seznamu něco je!')
else:
    print('V seznamu nic není!')

# Tak jako funkce int převádí na celá čísla a str na řetězce, funkce list (angl. seznam) převádí na seznam. Jako argument jí předáme jakoukoli hodnotu, kterou umí zpracovat příkaz for. Z řetězců udělá seznam znaků, z otevřeného souboru udělá seznam řádků, z range udělá seznam čísel.
abeceda = list('abcdefghijklmnopqrstuvwxyz')
cisla = list(range(100))
print(abeceda)
print(cisla)

# I ze seznamu udělá funkce list seznam. To může znít zbytečně, ale není – vytvoří se totiž nový seznam. Bude mít sice stejné prvky ve stejném pořadí, ale nebude to ten samý seznam: měnit se bude nezávisle na tom starém.
a = [1, 2, 3]
b = list(a)

print(b)
a.append(4)
print(a)
print(b)

# I ze seznamu udělá funkce list seznam. To může znít zbytečně, ale není – vytvoří se totiž nový seznam. Bude mít sice stejné prvky ve stejném pořadí, ale nebude to ten samý seznam: měnit se bude nezávisle na tom starém.
mocniny_dvou = []
for cislo in range(10):
    mocniny_dvou.append(2 ** cislo)
print(mocniny_dvou)

balicek = []
for barva in '♠', '♥', '♦', '♣':
    balicek.append(barva)
print(balicek)

# Seznamy a řetězce jsou druhy „sekvencí”, takže snad nepřekvapí, že se dá různě převádět z jednoho typu na druhý. Funkce list vytvoří z řetězce seznam znaků. Když chceme dostat seznam slov, použijeme na řetězci metodu split (angl. rozdělit):
slova = 'Tato věta je složitá, rozdělme ji na slova.'.split()
print(slova)

# Metoda split umí brát i argument. Pokud ho předáme, místo mezer (a nových řádků) se řetězec „rozseká” daným oddělovačem. Takže když máme nějaká data oddělená čárkami, není nic jednoduššího než použít split s čárkou:
zaznamy = '3A,8B,2E,9D'.split(',')
print(zaznamy)

# Chceme-li spojit seznam řetězců zase dohromady do jediného řetězce, použijeme metodu join (angl. spojit). Pozor, tahle metoda se volá na oddělovači, tedy řetězci, kterým se jednotlivé kousky „slepí” dohromady; a jako argument bere seznam jednotlivých řetězců.
veta = ' '.join(slova)
print(veta)


