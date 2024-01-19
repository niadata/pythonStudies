# Algoritimo para fatorar numeros
print("Fatoração")
print("---"*40)
n = int (input("Qual o número você deseja fatorar?"))

cont = 1
resultado = 1

while cont <= n:
    resultado*=cont
    cont+=1
print(resultado)
