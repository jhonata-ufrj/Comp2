#Nome: Jhonata Oliveira Da Silva
#DRE: 118153533

#Questão 1
casas = {1.1:"particular permanente", 1.2:"particular improvisado", 1.3:"coletivo"}
dicionario = {11281037702:1.1, 00000000000:1.2, 999999999:1.1, 888888888:1.3}#APAGAR DEPOIS

def frequenciaDomicilio(dicio):
    pp = 0 #Variável que representa a categoria de casa Particular Permanente
    pi = 0 #Variável que representa a categoria de casa Particular Improvisado
    ct = 0 #Variável que representa a categoria de casa Coletivo
    for i in dicio:
        if(dicio[i] == 1.1):
            pp += 1
        elif(dicio[i] == 1.2):
            pi += 1
        else:
            ct += 1   
    return {"Particular Permanente":pp, "Coletivo":ct, "Particular improvisado":pi}
    
print(frequenciaDomicilio({11281037702:1.1, 00000000000:1.2, 999999999:1.1, 888888888:1.3}))#APAGAR DEPOIS   

#Questão 2
dici = {100: {'geladeira', 'tv'}, 101: {'maquina', 'tv'}, 102: {'maquina'},
103: {'geladeira'}, 104: set()}
def processaDados(dicio):
    gl = {}
    tv = {}
    maq = {}
    lista = []
    for i in dicio:
        if('maquina' in dicio[i]):
            print(dicio.get(i))
    return lista

print(processaDados(dici))


"""for i in pessoa1:
    a = pessoa1[i]
    for x in a:
        if (b in a):
            print('ok')
        elif c in a:
            print('ok2') 
        elif d in a:
            print('ok3')     """  


