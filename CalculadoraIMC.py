def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura deve ser maior que 0 cm.")
    imc = peso / (altura / 100) ** 2
    return imc  


class imc:
    """Calculadora de IMC com classificação do resultado."""

    def calcular(self, peso, altura):
        return calcular_imc(peso, altura)

    def classificar(self, valor):
        if valor < 18.5:
            return "Abaixo do peso"
        if valor < 25:
            return "Peso normal"
        if valor < 30:
            return "Sobrepeso"
        if valor < 35:
            return "Obesidade grau I"
        if valor < 40:
            return "Obesidade grau II"
        return "Obesidade grau III"

    def calcular_e_classificar(self, peso, altura):
        valor = self.calcular(peso, altura)
        return valor, self.classificar(valor)           