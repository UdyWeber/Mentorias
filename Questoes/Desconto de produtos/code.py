DESCONTO_FIXO = 10


def calcular_desconto(valor: float, itens: int) -> float:
    percentual_de_desconto = (DESCONTO_FIXO + itens) / 100

    desconto_total = percentual_de_desconto * valor

    valor_com_desconto = valor - desconto_total

    print(round(valor_com_desconto, 2))


def calcular_preco(preco: float, qtd: int) -> float:
    valor = preco * qtd

    print(round(valor, 2))

    calcular_desconto(valor, qtd)

# Parte funcional para input do ususario, abaixo parte funcional com testes sugeridos na questao

# preco = input('Digite o valor: ')
# quantidade_de_mercadoria = input('Digite a quantidade de mercadoria: ')

# if not preco:
#     raise Exception('Preço não foi Informado')
#
# preco = float(preco)
#
# if not quantidade_de_mercadoria:
#     raise Exception('quantidade de mercadoria não foi Informado')
#
# if not quantidade_de_mercadoria.isdigit():
#     raise Exception('Quantidade de mercadoria informado não e valido')
#
# quantidade_de_mercadoria = int(quantidade_de_mercadoria)

tests = [
    (1.00, 40),
    (100.00, 10),
    (1000.00, 5),
    (56.75, 1),
    (1.50, 2),
    (2608542.45, 39)
]

for idx, tupla in enumerate(tests):
    preco, quantidade_de_mercadoria = tupla

    print("#"*30)

    print(f"Teste numero {idx + 1}")

    calcular_preco(preco, quantidade_de_mercadoria)

    print("#" * 30)
