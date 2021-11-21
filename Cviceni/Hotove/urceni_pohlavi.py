# Program, který se zeptá na příjmení uživatelky/uživatele a zkusí podle něj uhodnout její/jeho pohlaví.
prijmeni = input('Napiš své přijmení: ')
pohlavi = 'neznámé'

if 'ová' in prijmeni:
    pohlavi = 'žena'
    print('Myslím že jsi žena.')
else:
    print('Myslím že jsi muž.')
