barva_travy = 'zelená'
pocet_kotatek = 28

def popis_stav():
    return 'Tráva je {barva}. Prohání se po ní {pocet} koťátek'.format(
        barva = barva_travy, pocet = pocet_kotatek )