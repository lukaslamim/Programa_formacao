def Exercicio6():
    
    while(True):
        
        produto = input("Nome do produto: ")
        preco = float(input("Preço unitario: "))
        quantidade = int(input("Quantidade: "))

        if quantidade <= 10:
            
            total = preco * quantidade
            
        elif 11 <= quantidade <= 20:
            
            total = preco * quantidade * 0.90
            
        elif 21 <= quantidade <= 50:
            
            total = preco * quantidade * 0.80
            
        else:
            
            total = preco * quantidade * 0.75

        print(f"Produto: {produto}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor total: R${total:.2f}")

Exercicio6()
