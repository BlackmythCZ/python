# Typ objektu umí zjistit funkce type:
# type(0)
# type(True)
# type('abc')
# with open ('D:\\Git\\python\\Hesla\\token.txt') as f:
#    type(f)

# Většinu tříd jde v Pythonu zavolat, jako by to byly funkce, a vytvořit tak nový objekt dané třídy:
# trida_retezcu = type('abc')
# trida_retezcu(8)
# trida_retezcu([1, 2, 3])

# type('abcdefgh') == str

class Kotatko:
    def zamnoukej(self):
        print('Mňau!')
# definování druhého atributu:
    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňau, mňaou! {jidlo} mi chutná!")
# atribut s vynucenou hodnotou při založení objektu
    def __init__(self, jmeno):
        self.jmeno = jmeno
# Podobných „opodtržítkovaných“ (speciálních) metod je víc. Třeba metodu __str__ Python zavolá, když je potřeba převést objekt na řetězec:
    def __str__(self):
        return f'<Kotatko jmenem {self.jmeno}>'


# Vytvoření konkrétního objektu
kotatko = Kotatko('TEST')

# Volání metody
kotatko.zamnoukej()

# máš možnost si definovat vlastní atributy – informace, které se uloží k danému objektu. Atributy se označují tak, že mezi hodnotu a jméno jejího atributu napíšeš tečku:
mourek = Kotatko('Mourek')
# mourek.jmeno = 'Mourek'

micka = Kotatko('Micka')
# micka.jmeno = 'Micka'

print(mourek.jmeno)
print(micka.jmeno)

# Každá metoda má přístup ke konkrétnímu objektu, na kterém pracuje, právě přes argument self:

print('----------')
mourek.zamnoukej()
micka.zamnoukej()

mourek.snez('Ryba')
micka.snez('Mléko')

garfield = Kotatko('Garfield')
garfield.zamnoukej()

# Jako u jiných funkcí je možné jméno koťátka zadat buď jako pojmenovaný argument, nebo jako poziční.
# Obojí funguje stejně:
# mourek = Kotatko('Mourek')  # 'Mourek' je hodnota prvního argument pro __init__ (po self)
# micka = Kotatko(jmeno='Micka')  # 'Micka' je hodnota argumentu `jmeno`

garfield.__str__()