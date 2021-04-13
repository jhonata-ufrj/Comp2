#Nome: Jhonata Oliveira da Silva
#DRE: 118153533
import math

#Questão 1:
def calculeN(a1,an,r):
    n = ((an - a1) / r) + 1
    return n

def somaPA(a1,an,r):
    sn = ((a1+an) * calculeN(a1,an,r)) / 2
    return sn

print(somaPA(1,100,5))


#Questão 2:
def concatena():
    txt1 = input('Digite uma sentença: ')
    if(len(txt1) < 15):
        print('Sentença com menos de 15 caracteres')
        txt1 = input('Digite a sentença novamente: ')

    txt2 = input('Digite outra sentença: ')
    if(len(txt2) < 15):
        print('Sentença com menos de 15 caracteres')
        txt2 = input('Digite a sentença novamente: ')
    return (txt1[5:] + txt2[0:len(txt2) - 10])

print(concatena())


#Questão 3:
def sublista(lista,n):
    sublista = []
    for i in range(len(lista)):
        if(lista[i] > n):
            print(lista[i])
            sublista.append(lista[i])
    return sublista

print(sublista([27,94352,45,64,10,11,12325,15,87,92],50))


#Questão 4:
def primo(n):
    primo = 0
    for i in range(1, n+1):
        if(n%i == 0):
            primo += 1
    if(primo > 2):
        print('O numero informado nao eh primo')
    else:
        print('O numero informado eh primo')

primo(7)


#Questão5:
def numeroEuler(n):
    e = 0
    for i in range(n+1):
        e += (1/math.factorial(i))     
    return e

def precisaoEuler(erro):
    erroAbs = math.fabs(math.e - numeroEuler(0))
    i = 0
    while(erroAbs >= erro):
        i+= 1
        erroAbs = math.fabs(math.e - numeroEuler(i))
    return i

print(precisaoEuler(0.000097))

def main():
    erro = float(input("Digite o erro máximo a ser tolerado: "))
    print(precisaoEuler(erro))

if __name__ == "__main__":
    main()