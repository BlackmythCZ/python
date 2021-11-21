from random import randrange


while True:
    tah_pc = randrange(3)
    tah_hrace = input(print('Napiš svůj tah: '))

    if tah_hrace == 'konec':
        break
    
    while True:
        if tah_hrace == 'kámen' or tah_hrace == 'nůžky' or tah_hrace == 'papír':
            break
        else:
            tah_hrace = input(print('Napiš buď kámen, nůžky nebo papír. Nic jiného!'))

    if tah_pc == 0:
        tah_pc = 'kámen'
    elif tah_pc == 1:
        tah_pc = 'nůžky'
    else:
        tah_pc = 'papír'

    print(f"Počítač si vybral: {tah_pc}.")


    if tah_pc == tah_hrace.lower():
        print('Plichta!')
    elif (tah_pc == 'kámen' and tah_hrace == 'nůžky') or (tah_pc == 'nůžky' and tah_hrace == 'papír') or (tah_pc == 'papír' and tah_hrace == 'kámen'):
        print('Prohrál jsi!')
    else:
        print('Vyhrál jsi!')