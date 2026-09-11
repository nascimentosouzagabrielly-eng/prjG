produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o desconto (%): "))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print(f"O produto {produto} custa R$ {preco_final:.2f} com desconto!")