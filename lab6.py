#Questão1
"""Função que compara a similaridade de duas strings"""
def compararStrings(str1, str2):
    try:
        str1 = str1.replace(" ", "")#função que substitui, na string, um valor passado no primeiro
        str2 = str2.replace(" ", "")#argumento por um valor passado no segundo
        if(len(str1) < len(str2)):#if que verifica qual é a menor string
            strcurta = str1
        else:
            strcurta = str2
        contador = 0
        for i in range(len(str1)): #FOR que varre a primeira string e verifica se o termo do momento
            if(str1[i] == str2[i]):#é igual ao termo de mesmo índice da segunda string
                contador += 1
        return contador / len(strcurta)
    except IndexError:#tratamento de exceção que evita o INDEXERROR quando uma string é menor do que a outra
        return contador / len(strcurta)

#Questão2
"""Função que recebe um arquivo e retorna uma lista do conteúdo recebido sem as linhas vazias(\n),
e também sem as linhas que começam por '#' """
def lerArquivo(texto):
    arquivoaux = open(texto, "r")#variável auxiliar que irá receber o arquivo de texto passado como parâmetro
    arquivo = arquivoaux.read()#variável definitiva que lê o conteúdo do arquivo em formato str
    #Criação de listas que serão manipuladas dentro dos loops e condicionais
    listaux = []
    lista = []
    listafinal = []
    for i in range(len(arquivo)):#laço de repetição que junta os arquivos no formato str em elementos de uma lista
        #condicional que adiciona à lista somente os caracteres dentro das condições estabelecidas
        if(arquivo[i] != "\n" and arquivo[i] != "\n#"):
                listaux.append(arquivo[i])
        else:
            listaux = ''.join(listaux)
            lista.append(listaux)
            listaux = []
    for j in range(len(lista)):#laço de repetição que adiciona os elementos tratados à uma lista final
        if(lista[j] != "" and lista[j][0] != "#"):#último condicional que elimina o restante dos elementos indesejados
            listafinal.append(lista[j])
    arquivoaux.close()
    return listafinal

#Questão3
"""Função que recebe dois arquivos, chama a função 'lerArquivo' e retorna a soma das similaridades
dos dois arquivos(por meio da 'compararStrings') dividida pelo tamanho da menor lista"""
def compararArquivos(arq1, arq2):
    try:
        a1 = lerArquivo(arq1)
        a2 = lerArquivo(arq2)
        aux = 0
        if(len(a1) < len(a2)):
            strcurta = len(a1)
            strlonga = len(a2)
        else:
            strcurta = len(a2)
            strlonga = len(a1)
        for i in range(strlonga):
            aux += compararStrings(a1[i],a2[i])
        return aux / strcurta
    except IndexError:#tratamento de exceção para divergência entre os tamanhos das listas
        return aux / strcurta

#Questão4
"""Função que recebe uma lista com nomes de arquivos e retorna um outro arquivo com os detalhes
da comparação entre todos os arquivos presentes na lista"""
def descobrirCola(lista):
    resultado = open("resultado.txt", "w")
    aux = 0
    try:
        for i in range(0, len(lista)):
            j = i + 1
            while j < len(lista):
                aux = compararArquivos(lista[i], lista[j])
                resultado.write("{} com {} deu {}\n".format(lista[i], lista[j], aux))
                j += 1
        resultado.close()
        return resultado
    except IndexError:#tratamento de exceção para divergência entre os tamanhos das listas
        return resultado

