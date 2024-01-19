# Algoritimo para retorna a sequência de fibonnaci
print("Lista da sequência de Fibonnaci")
print("-"*40)
n = int (input("Quantos números devem ser mostrados:"))
s1 = 0
s2 = 1
print('{}'.format(s1), end='')
cont = 2
while cont <= n:
    s3 = s1+s2
    print('-> {}'.format(s3), end='')
    s1 = s2
    s2 = s3
    cont += 1
print ('-> Fim da sequência')
