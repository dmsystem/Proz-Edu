def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def mostrar_opcoes():
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

def calculadora():
    while True:
        mostrar_opcoes()
        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == '0':
            print("Saindo da calculadora...")
            break
        elif opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe.")
            continue

        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Valores inválidos. Tente novamente.")
            continue

        if opcao == '1':
            resultado = soma(num1, num2)
        elif opcao == '2':
            resultado = subtracao(num1, num2)
        elif opcao == '3':
            resultado = multiplicacao(num1, num2)
        elif opcao == '4':
            resultado = divisao(num1, num2)

        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    calculadora()
