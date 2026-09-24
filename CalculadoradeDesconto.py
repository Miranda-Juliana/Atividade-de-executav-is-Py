def calcular_desconto(preco, porcentagem, quantidade, desconto_maximo):
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    if porcentagem < 0 or porcentagem > 100:
        raise ValueError("A porcentagem de desconto deve ter entre 0 e 100")
    desconto = preco * (porcentagem / 100)
    return min(desconto, desconto_maximo) * quantidade  