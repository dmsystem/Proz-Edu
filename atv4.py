def calcular_idade(ano_nascimento):
    ano_atual = 2022
    return ano_atual - ano_nascimento

def receber_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento inválido. Digite novamente.")
        except ValueError:
            print("Ano de nascimento inválido. Digite novamente.")

def main():
    nome_completo = input("Digite seu nome completo: ")

    while True:
        try:
            ano_nascimento = receber_ano_nascimento()
            idade = calcular_idade(ano_nascimento)
            break
        except ValueError:
            print("Ano de nascimento inválido. Digite novamente.")

    print(f"Nome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")

if __name__ == "__main__":
    main()
