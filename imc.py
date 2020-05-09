#Programa calculando (IMC) indice e massa corporal
def pessoa():
    print(f'Olá {nome} vamos calcular seu IMC: ')


#calculando 0 IMC
def imc(altura, peso):
    indec = peso / altura ** 2
    if indec < 18.5:
        print(f'O seu IMC é {indec:.1f}\nClassificação \33[1:33:41mMAGREZA\33[m!')
    elif 18.5 <= indec < 24.9:
        print(f'O seu IMC é {indec:.1f}\nClassificação \33[30:42mNORMAL\33[m!')
    elif 24.9 <= indec < 29.9:
        print(f'O seu IMC é {indec:.1f}\nClassificação \33[1:35:43mSOBREPESO\33[m!')
    elif 29.9 <= indec < 39.9:
        print(f'O seu IMC é {indec:.1f}\nClassificação \33[1:33:41mOBESIDADE\33[m!')
    else:
        print(f'O seu IMC é {indec:.1f}\nClassificação \33[1:33:41mOBESIDADE GRAVE\33[m!')


nome = str(input('Digite seu nome: ')).upper()
pessoa()
alt = float(input('Digite sua altura (m): '))
pes = float(input('Digite seu peso (Kg):'))
imc(alt, pes)



