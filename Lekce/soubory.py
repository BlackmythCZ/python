
# Načtení souboru příkazem with:
'''
with open('D:\\Git\\python\\Lekce\\Data\\basnicka.txt', encoding='utf-8') as soubor:
    obsah = soubor.read()

print(obsah)
'''

# Výpis obsahu souboru po řádcích:

'''
print('Slyšel jsem tuto básničku:')
print()

with open('D:\\Git\\python\\Lekce\\Data\\basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        radek = radek.rstrip() #dstraní z konce řetězce bílé znaky (mezery a nové řádky) pomocí metody rstrip
        print('' + radek)

print()
print('Jak se ti líbí?')
'''

#Soubory se v Pythonu dají i zapisovat. Pro zápis soubor otevři s pojmenovaným argumentem mode='w' (z angl. mode, mód a write, psát).
#Pokud soubor už existuje, otevřením s mode='w' se veškerý jeho obsah smaže. Po zavření tak v souboru bude jen to, co do něj ve svém programu zapíšeš.
# Informace pak do souboru zapiš známou funkcí print, a to s pojmenovaným argumentem file:

with open('D:\\Git\\python\\Lekce\\Data\\druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
    print('Naše staré hodiny', file = soubor)
    print('Bijí', 2+2, 'hodiny', file = soubor)

