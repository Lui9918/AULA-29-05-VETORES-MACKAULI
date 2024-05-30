#Faça um programa que peça o nome e a idade de 5 pessoas, armazene cada informação em seu respectivo vetor
#Imprima o nome e a idade na ordem lida.

if __name__ == '__main__':
    print("Bem vindo ao programa")

#Criar variavel nome
    nomes = []
    contador = 0

    while (contador <= 4):
        nome = input("Digite um nome: ")
        nomes.append(nome) #estou adiconando num ao vetor
        contador = contador + 1
        print ("Nome registrado!")

    #Imprimir o vetor na tela

    i = 0

    while (i <= 4):
        print(nomes[i])
        i = i + 1

    print("Agora informe as idades de cada pessoas na ordem dos nomes: ")

    #Criar variavel idade
    idades = []
    contador = 0

    while (contador <= 4):
        idade = int(input("Digite a idade: "))
        idades.append(idade) #estou adiconando num ao vetor
        contador = contador + 1
        print ("Idade registrada!")

    #Imprimir o vetor na tela

    i = 0

    while (i <= 4):
        print(idades[i])
        i = i + 1

    print("O nome e idade da primeira pessoa é: ")
    print(f"{nomes[0]}, {idades[0]}")

    print("O nome e idade da segunda pessoa é: ")
    print(f"{nomes[1]}, {idades[1]}")

    print("O nome e idade da terceira pessoa é: ")
    print(f"{nomes[2]}, {idades[2]}")

    print("O nome e idade da quarta pessoa é: ")
    print(f"{nomes[3]}, {idades[3]}")

    print("O nome e idade da quinta pessoa é: ")
    print(f"{nomes[4]}, {idades[4]}")
