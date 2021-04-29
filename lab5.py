#Aluno: Jhonata Oliveira Da Silva
#DRE: 118153533

#Questão 1: 
"""Função que, ao receber números inteiros e floats, puros ou passados como strings, retorna
o valor absoluto do mesmo no tipo de dado Float"""
def positivo(n):
    try:
        return abs(float(n))
    except ValueError:
        print("'{}' não pode ser convertido em um número".format(n))
        return None
    except TypeError:
        print("'{}' não pode ser convertido em um número".format(n))
        return None       

#Questão 2:
"""Função que, ao receber uma lista e um elemento, busca todas as aparições do elemento na lista
fornecida como parâmetro e retorna outra lista contendo seus índices. Caso o elemento não esteja
na lista, uma lista vazia é retornada """
def encontraIndices(lista,n):
    idc = []
    j = -1
    for i in range(len(lista)):
        try:
               j = lista.index(n, j+1, len(lista))
               idc.append(j)
        except ValueError:
            break
    return idc
    
#Questão 3:
"""Função que, ao receber uma tupla como parâmetro, retorna uma lista contendo a divisão de 1
por cada elemento presente na tupla, caso estes elementos satisfaçam as condições necessárias
para que ocorra a divisão """
def inversos(tupla):
    lista = []
    str = ""
    for i in range(len(tupla)):
        try:
            lista.append(1 / float(tupla[i]))   
        except TypeError:
            str += "Entrada de tipo {} não válida\n".format(type(tupla[i]))
            lista.append("Nan") 
        except ValueError:
            str += "Inverso de '{}' não definido".format(tupla[i])
            lista.append("Nan")
        except ZeroDivisionError:
            str += "Divisão por zero\n"
            lista.append("Nan") 
    return '{}{}'.format(str, lista)

  