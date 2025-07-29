def analisar_numeros():
    numeros_pares = 0
    numeros_impares = 0

    print("--- Análise de Números Pares e Ímpares ---")
    print("Digite um número por vez. Digite 'fim' para encerrar.")

    while True:
        entrada = input("Digite um número (ou 'fim' para sair): ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                numeros_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                numeros_impares += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido ou 'fim'.")

    print("\n--- Resultados Finais ---")
    print(f"Total de números pares inseridos: {numeros_pares}")
    print(f"Total de números ímpares inseridos: {numeros_impares}")
    print("Obrigado por usar o programa!")

analisar_numeros()