# Třída pro koťátka:
class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")
    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")
# Třída pro štěňátka:
class Stenatko:
    def __init_(self, jmeno):
        self.jmeno = jmeno
    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")
    def zastekej(self):
        print(f"{self.jmeno}: Haf!")

# Většina kódu je stejná, můžeme vytvořit třídu společnou pro všechna zvířátka:

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")

# definice nové třídy (podtřídy) s děděním (rozšířením) z nadřazené:
class Lemur(Zviratko):
    def psoukni(self):
        print(f"{self.jmeno}: Prrrrrd!")

prdola = Lemur('Prďola')
prdola.psoukni()

