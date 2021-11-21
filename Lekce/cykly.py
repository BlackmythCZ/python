'''JMENO'''

'''for i in range(100):
    print('Nikdy nebudu odsazovat o tři mezery!')

for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':
    print(pozdrav + '!')

for i in range(5):
    print(i)
'''

'''from turtle import forward, penup, pendown, exitonclick

for _ in range(20):
    forward(10)
    penup()
    forward(5)
    pendown()
exitonclick()

for _ in range(20):
    forward(_)
    penup()
    forward(5)
    pendown()
exitonclick()'''

'''from turtle import forward, exitonclick, left

for _ in range(3):
    for __ in range(4):
        forward(50)
        left(90)
    left (20)    
exitonclick()
'''

'''odpoved = input('Řekni Ááá! ')
while odpoved != 'Ááá':
    print('Špatně, zkus to znovu')
    odpoved = input('Řekni Ááá! ')
'''

'''from random import randrange

while True:
    print('Číslo je', randrange(10000))
    print('Počkej, než se počítač unaví...')
'''

'''
while True:
    odpoved = input('Řekni Ááá! ')
    if odpoved == 'Ááá':
        print('bééé')
        break
    print('Špatně, zkus to znovu')
print('Hotovo. Ani to nebolelo.')
'''

'''celkem = 0

for delka_trasy in 8, 45, 9, 21:
    print('Jdu', delka_trasy, 'km do další vesnice.')
    celkem = celkem + delka_trasy

print('Celkem jsem ušel', celkem, 'km.')

TEST GITU
TEST GIT branches
'''

'''print(len('\N{SNOWMAN}ové'))
print('\N{SNOWMAN}ové')

if True:
    print(len("""a
 b"""))

print(len(f'{print}'))
'''

retezec = 'čokoláda'
print(retezec[:4])
print(retezec[2:6])
print(retezec[-3:])
print(retezec[:])

