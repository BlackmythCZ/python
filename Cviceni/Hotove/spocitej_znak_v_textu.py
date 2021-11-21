# Program projde vložený text a spočítá kolikrát se v něm vyskytuje zvolený znak.

text = input(print('Vlož text, ve kterém chceš spočítat výskyt znaku: '))
znak = input(print('Jaký znak chce spočítat: '))
pocet_vyskytu=0

print(f'Znak {znak} se v textu vyskytuje {text.count(znak)}krát.')