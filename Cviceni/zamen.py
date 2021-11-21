slovo = ''
pozice = int()
novy_znak = ''
def zamen(slovo, pozice, novy_znak):
    nove_slovo = slovo[:pozice] + novy_znak + slovo[pozice+1:]
    return nove_slovo

# print(zamen(slovo, pozice, novy_znak))