def divi1(n1, n2):
    return n1 / n2

def divi2(n1, n2):
    try:
        return float(n1) / float(n2)
    except ZeroDivisionErr
        print("erro... operação iválida")
        return None
    except ValueError:
        print("A função trabalha com duas entradas numéricas")
        return None
"""print(divi1(6.7, 2))
print("-------------")
#print(divi1("a", 2)) TYPE ERROR   
print("-------------")
#print(divi1(2, 0)) ZERO DIVISION ERROR
print("-------------")
print(divi1(0, 2))"""

print(divi2(6.7, 2))
print("-------------")
print(divi2("a", 2)) 
print("-------------")
print(divi2(2, 0))
print("-------------")
print(divi2(0, 2))