import CalculadoraIMC
import CalculadoradeDesconto
import Appnumeroprimo
import Conversordetemperatura


def main ():
    while True:
        print("Menu de Opções:")
        print("1. Calculadora de IMC")
        print("2. Calculadora de Desconto")
        print("3. Verificar se um número é primo")
        print("4. Converter Temperatura")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            peso = float(input("Digite o peso em kg: "))
            altura = float(input("Digite a altura em cm: "))
            try:
                imc = CalculadoraIMC.calcular_imc(peso, altura)
                classificacao = CalculadoraIMC.imc().classificar(imc)
                print(f"Seu IMC é: {imc:.2f} (classificação: {classificacao})")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            try:
                preco = float(input("Digite o preço do produto: "))
                porcentagem = float(input("Digite a porcentagem de desconto: "))
                quantidade = int(input("Digite a quantidade: "))
                desconto_maximo = float(input("Digite o desconto máximo permitido: "))
                desconto_total = CalculadoradeDesconto.calcular_desconto(preco, porcentagem, quantidade, desconto_maximo)
                print(f"O desconto total é: {desconto_total:.2f}")
            except ValueError as e:
                print(e)

        elif opcao == "3":
            numero = int(input("Digite um número para verificar se é primo: "))
            if Appnumeroprimo.eh_primo(numero):
                print(f"{numero} é um número primo.")
            else:
                print(f"{numero} não é um número primo.")

        elif opcao == "4":
            temperatura = float(input("Digite a temperatura: "))
            unidade_origem = input("Digite a unidade de origem (C/F): ")
            unidade_destino = input("Digite a unidade de destino (C/F): ")
            try:
                temperatura_convertida = Conversordetemperatura.converter_temperatura(temperatura, unidade_origem, unidade_destino)
                print(f"A temperatura convertida é: {temperatura_convertida:.2f} {unidade_destino}")
            except ValueError as e:
                print(e)

        elif opcao == "5":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

            

def classificar_imc(imc):
    """Retorna a classificação correspondente ao valor do IMC."""
    if not isinstance(imc, (int, float)) or imc < 0:
        raise ValueError("O IMC deve ser um número não negativo.")

    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"



if __name__ == "__main__":
    main()