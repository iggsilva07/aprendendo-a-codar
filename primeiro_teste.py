num_pol = list(range(0, 25))
boasVindas = 'Ola seja bem vindo! escolha uma poltrona livre.'


def painel():
    print('=' * 60)
    print(boasVindas)
    print('='*60)


painel()
for pol in num_pol:
    print(f'[{pol}]', end=' ')
    if pol == 13:
        print('\n')#escolha fora do laço

print()
print('='*60)
num = int(input('\n\nEscolha uma poltrona: '))

num_pol.index(num)
num_pol.insert(num, 'X')
num_pol.remove(num)

while True:#lopp de escolha das poltronas
    for pol in num_pol:
        print(f'[{pol}]', end=' ')

        if pol == 13:
            print('\n')
    print()
    num = int(input('\n\nEscolha uma poltrona: '))
    num_pol.index(num)
    num_pol.insert(num, 'X')
    num_pol.remove(num)



