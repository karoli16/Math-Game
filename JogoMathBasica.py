from random import randint

opcao = """
Selecione uma opção:
[s] = soma
[m] = subtração
[v] = multiplicação
[q] = sair
"""

def soma():
    n1 = randint(10, 500)
    n2 = randint(10, 500)
    
    print(" ", n1, end=" +")
    print(" ", n2)
    
    resposta = int(input("Digite sua resposta: "))
    if resposta == n1 + n2:
        print("Parabéns!!")
    else:
        print("Resposta está errada!")
        print("A resposta certa é: ")
        print(" ", n1 + n2)

def subtracao():
    n1 = randint(5, 50)
    n2 = randint(5, 50)
    
    n1, n2 = max(n1, n2), min(n1, n2)

    print(" ", n1, end=" -")
    print(" ", n2)
    
    resposta = int(input("Digite sua resposta: "))
    if resposta == n1 - n2:
        print("Parabéns!!")
    else:
        print("Resposta está errada!")
        print("A resposta certa é: ")
        print(" ", n1 - n2)

def multiplicacao():
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    
    print(" ", n1, end=" x")
    print(" ", n2)
    
    resposta = int(input("Digite sua resposta: "))
    if resposta == n1 * n2:
        print("Parabéns!!")
        
    else:
        print("Resposta está errada!")
        print("A resposta certa é: ")
        print(" ", n1 * n2)
      

# Laço de repetição para o jogo
while True:
   
    print(opcao)
    escolha = input('Sua escolha:..')
    if escolha == 's':
        soma()
    elif escolha == 'm':
        subtracao()
    elif escolha == 'v':
        multiplicacao()
    elif escolha == 'q':
        print("Você escolheu sair. Até a próxima!")
        break
    else:
        print("Opção inválida! Tente novamente.")