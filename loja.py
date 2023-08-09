def ir_para_loja(personagem):
    print("Bem-vindo à Loja!")
    print(f"Moedas possuídas: {personagem['dinheiro']}")
    print("Itens disponíveis:")
    print("[1] - Poção de Vida (+20 de vida) - 10 moedas")
    print("[2] - Espada Melhorada (+10 de dano) - 20 moedas")
    print("[3] - Armadura Reforçada (+30 de vida máxima) - 30 moedas")
    print("[4] - Poção de Sono (Deixa o inimigo dormindo) - 15 moedas")
    print("[5] - Sair da loja")

    while True:
        escolha = input("Escolha um item para comprar (ou digite '5' para sair): ")

        if escolha == "1":
            if personagem["dinheiro"] >= 10:
                personagem["vida"] += 20
                personagem["dinheiro"] -= 10
                print("Você comprou uma Poção de Vida! Sua vida aumentou em 20.")
            else:
                print("Dinheiro insuficiente para comprar este item.")
        elif escolha == "2":
            if personagem["dinheiro"] >= 20:
                personagem["ataque"] += 10
                personagem["dinheiro"] -= 20
                print("Você comprou uma Espada Melhorada! Seu dano aumentou em 10.")
            else:
                print("Dinheiro insuficiente para comprar este item.")
        elif escolha == "3":
            if personagem["dinheiro"] >= 30:
                personagem["vida"] += 30
                personagem["vida_maxima"] += 30
                personagem["dinheiro"] -= 30
                print("Você comprou uma Armadura Reforçada! Sua vida e vida máxima aumentaram em 30.")
            else:
                print("Dinheiro insuficiente para comprar este item.")
        elif escolha == "4":
            if personagem["dinheiro"] >= 15:
                personagem["pocao_sono"] += 1
                personagem["dinheiro"] -= 15
                print("Você comprou uma Poção de Sono! Use-a com sabedoria.")
            else:
                print("Dinheiro insuficiente para comprar este item.")
        elif escolha == "5":
            print("Você saiu da loja.")
            break
        else:
            print("Opção inválida! Por favor, escolha um item válido.")
