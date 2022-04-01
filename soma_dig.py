
# Programa para ler um número de entrada e somar os dígitos desse número.


# Exemplo:  546 - soma= 15

numero=int(input("Entre com um número inteiro positivo: "))

soma=0
if (numero>=10):
      while (numero//10!=0):
             soma=soma+numero%10
             numero=numero//10
             if numero<10:
                  soma=soma+numero%10
else:
      soma=numero
print(soma)          