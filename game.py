import random


def main():
    erros = int()
    contador = int()

    palavras = ["banana", "abacaxi", "melao", "morango", "futebol", "pernambuco", "geladeira"]

    indice = random.randint(1, len(palavras) - 1)

    palavra_da_vez = palavras[indice]

    linha = "_" * len(palavra_da_vez)

    print(linha)

    painel(palavra_da_vez, None, linha)

    result = resultado(linha)

    while erros <= 5:

        letra = input("Digite uma letra: ")

        if letra in palavra_da_vez:
            print(f"{letra} está na palavra secreta!")

            linha = painel(palavra_da_vez, letra, linha)
        else:
            erros += 1
            print(f"{letra} não está na palavra secreta!")
            linha = painel(palavra_da_vez, None, linha)

        contador += 1

        result = resultado(linha)

        print(linha)

        if result:
            break

    if result:
        print("Ganhou!!!")
    else:
        print("Perdeu!!!")
        print(f"A palavra era {palavra_da_vez}")


def painel(palavra_da_vez, letra, linha):
    linha_list = list(linha)

    if letra is not None:
        for i in range(0, len(palavra_da_vez)):
            if letra == palavra_da_vez[i]:
                linha_list[i] = letra

    return "".join(linha_list)


def resultado(linha):
    ganhou = True

    if "_" in linha:
        ganhou = False

    return ganhou


if __name__ == "__main__":
    main()
