# Testy, které kontrolují reakci na „špatný“ vstup, se jmenují negativní testy. Můžou kontrolovat nějaký negativní výsledek (např. že volání jako cislo_je_sude(7) vrátí False), a nebo to, že nastane „rozumná“ výjimka.
# Například funkce tah_pocitace by měla způsobit chybu (třeba ValueError), když je herní pole už plné.

import pytest
import piskvorky1d

def test_tah_chyba():
    with pytest.raises(valueError):
        piskvorky1d.tah_pocitace('oxoxoxoxoxoxoxoxoxox')
