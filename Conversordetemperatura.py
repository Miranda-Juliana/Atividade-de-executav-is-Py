def converter_temperatura(valor, unidade_origem, unidade_destino):
    if unidade_origem == "C" and unidade_destino == "F":
        return (valor * 9/5) + 32
    elif unidade_origem == "F" and unidade_destino == "C":
        return (valor - 32) * 5/9
    elif unidade_origem == "C" and unidade_destino == "K":
        return valor + 273.15
    elif unidade_origem == "K" and unidade_destino == "C":
        return valor - 273.15
    elif unidade_origem == "F" and unidade_destino == "K":
        return (valor - 32) * 5/9 + 273.15
    elif unidade_origem == "K" and unidade_destino == "F":
        return (valor - 273.15) * 9/5 + 32
    else:
        raise ValueError("Unidade de origem ou destino inválida.")