#Faça um programa que leia 4 notas, mostre as notas e média na tela.

if __name__ == '__main__':
    print("Bem vindo ao programa")

#Ler as notas
    notas = []
    contador = 0

    while (contador < 4):
        nota = int(input("Digite uma nota: "))
        notas.append(nota) #estou adiconando num ao vetor
        contador = contador + 1
        print ("Nota contabilizada!")

    #Imprimir o vetor na tela

    i = 0

    while (i < 4):
        print(notas[i])
        i = i + 1

    print(f"Suas notas são: ")
    print(notas[0],notas[1],notas[2],notas[3])

    soma_notas = (notas[0] + notas[1] + notas[2] + notas[3])

    resultado = soma_notas / 4

    print("A media de notas é: ")
    print(resultado)




