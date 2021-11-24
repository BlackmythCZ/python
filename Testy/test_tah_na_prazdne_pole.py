# Testům, které kontrolují, že se program za správných podmínek chová správně, se říká pozitivní testy. Test může vypadat třeba takhle:

import piskvorky1d

def test_tah_na_prazdne_pole()
    pole = piskvorky.tah_pocitace('--------------------')
    assert len(pole) == 20
    assert pole.count('x') == 1
    assert pole.count('-') == 19
