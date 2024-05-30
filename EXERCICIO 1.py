1#Faça um programa que leia um vetor de 5 numeros inteiros e mostre-os

if __name__ == '__main__':
    #creat one empty vetor

    numbers = []

    contador = 0
    while (contador < 5):
        num = int(input("Insira um numero "))
        numbers.append(num) #estou adiconando num ao vetor
        contador = contador + 1
        print ("Leitura finalizada!")

    #Imprimir o vetor na tela

    i = 0

    while (i < 5):
        print(numbers[i])
        i = i + 1

    print ("Ordem inversa:")

    i = 4

    while (i >= 0):
        print(numbers[i])
        i = i - 1
