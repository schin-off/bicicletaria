"""
1. Cadastrar Peça X
2. Consultar Peça
    1) Consultar Todas as Peças X
    2) Consulta Peças por Código X
    3) Consulta Peças por Fabricante x
    4) Retornar X
3. Remover Peça X
4. Sair X
"""

pecas = [] #a lista onde vai as peças
codigo = 1 #o código para que cada peça tenha seu código unico

def cadastrar_pecas(): #a função para cadastrar a peça
    print("Claro, por favor...")
    nome = input("Digite o nome da peça: ") #pega os dados
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))

    peca = { #o dicionario onde vai as expecificações da peça
        "codigo": codigo,
        "nome": nome,
        "fabricante": fabricante,
        "valor": valor
    }

    pecas.append(peca) # adiciona na lista
    print("Peça adicionada com sucesso!\n")

def remover_peca(): #a função para remover a peça
    codigo1 = int(input("\nDigite o código da peça que deseja remover: "))
    for peca in pecas: #um looping para conferir cada peça da lista
        if peca["codigo"] == codigo1:
            pecas.remove(peca)
            print("\nPeça removida com sucesso.")
            break
    else: #caso não tenha alguma peça com este código aparece este print
        print("Peça não encontrada.")

def consultar_peca(): #a função para pesquisar as peças
    while True: # um looping para não sair desta opção a menos que queiraa
        consulta = int(input("Você deseja...\n1) Consultar Todas as Peças\n2) Consulta Peças por Código\n3) Consulta Peças por Fabricante\n4) Retornar\n"))
        if consulta == 1: #para pesquisar todas peças
            print("------------------------\n")
            if len(pecas) > 0: #caso a lista seja mair que zero aparece todas peças
                for peca in pecas:
                    print(f"Código: {peca['codigo']}")
                    print(f"Nome: {peca['nome']}")
                    print(f"Fabricante: {peca['fabricante']}")
                    print(f"Valor: R${peca['valor']:.2f}\n")
            else:
                print("Não há peças cadastradas.\n3") #caso seja 0 aparece este print
            print("------------------------")
        elif consulta == 2: #para pesquisar por código
            consulta1 = int(input("Qual é o código da peça? "))
            encontrada = False #uma forma de teste para caso o input não entre dentro deste loop e transforme em true
            for peca in pecas:
                if peca["codigo"] == consulta1:
                    print("------------------------")
                    print(f"Código: {peca['codigo']}")
                    print(f"Nome: {peca['nome']}")
                    print(f"Fabricante: {peca['fabricante']}")
                    print(f"Valor: R${peca['valor']:.2f}")
                    print("------------------------")
                    encontrada = True
                    break
            if not encontrada: #e caso não entre aparece isto
                print("Peça não encontrada.")
        elif consulta == 3: #para procurar por fabricante
            consulta1 = input("Qual é o nome do fabricante? ")
            encontrada = False
            for peca in pecas:
                if peca["fabricante"] == consulta1:
                    print("------------------------")
                    print(f"Código: {peca['codigo']}")
                    print(f"Nome: {peca['nome']}")
                    print(f"Fabricante: {peca['fabricante']}")
                    print(f"Valor: R${peca['valor']:.2f}")
                    print("------------------------")
                    encontrada = True
            if not encontrada:
                print("Peça não encontrada")
        elif consulta == 4: #para sair deste looping e voltar ao principal
            break

print("Bem vindo ao controle de estoque da Bicicletaria do Gabriel Schinoff!!") # o identificador
while True: #o looping principal
    try: #um teste para caso aconteça alguma erro
        a = int(input("O que deseja fazer?\n1) Cadastrar peça\n2) Remover peça\n3) Consultar peças\n4) Sair\n"))
        if a == 1:
            cadastrar_pecas() #as respectivas funções
            codigo += 1
        elif a == 2:
            remover_peca()
        elif a == 3:
            consultar_peca()
        elif a == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, digite um número válido.")
    except ValueError:
        print("Opção inválida. Por favor, digite um número inteiro.")