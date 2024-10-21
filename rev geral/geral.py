class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.total = preco * quantidade

    def __str__(self):
        return f"{self.nome}: R${self.preco:.2f} x {self.quantidade} = R${self.total:.2f}"

class ListaDeCompras:
    def __init__(self):
        self.produtos = []
        self.totalProdutos = 0

    def adicionar(self, nome, preco, quantidade):
        produto = Produto(nome, preco, quantidade)
        self.produtos.append(produto)
        self.atualizar_total()

    def visualizar(self):
        if not self.produtos: 
            print("\033[33mNenhum item adicionado.")  
        else:
            for produto in self.produtos:
                print("\033[32m" + str(produto)) 
            print("\033[36mTotal: R${:.2f}".format(self.totalProdutos))  

    def atualizar(self, nome, novo_nome=None, novo_preco=None, nova_quantidade=None):
        for produto in self.produtos:
            if produto.nome == nome:
                if novo_nome is not None:
                    produto.nome = novo_nome
                if novo_preco is not None:
                    produto.preco = novo_preco
                if nova_quantidade is not None:
                    produto.quantidade = nova_quantidade
                produto.total = produto.preco * produto.quantidade
                self.atualizar_total()
                return
        print("\033[31mItem não encontrado.")  

    def remover(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                self.atualizar_total()
                return
        print("\033[31mItem não encontrado.")  

    def atualizar_total(self):
        self.totalProdutos = sum(produto.total for produto in self.produtos)

lista = ListaDeCompras()
while True:
    print("\033[34mSelecione uma opção:") 
    print("1 - Adicionar Item")
    print("2 - Visualizar itens")
    print("3 - Remover Item")
    print("4 - Atualizar Item")
    print("5 - Encerrar Programa.")

    opcao = input("\033[36m << Escolha uma opção >> ")  

    if opcao == "1":
        nome = input("Nome do item: ")
        preco = float(input("Digite o preço do item: "))
        quantidade = int(input("Digite a quantidade do item: "))
        lista.adicionar(nome, preco, quantidade)
    elif opcao == "2":
        lista.visualizar()
    elif opcao == "3":
        nome = input("Digite o nome do item que deseja remover: ")
        lista.remover(nome)
    elif opcao == "4":
        nome = input("Digite o nome do item que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do item (deixe em branco se não quiser mudar): ")
        novo_preco = input("Digite o novo preço do item (deixe em branco se não quiser mudar): ")
        nova_quantidade = input("Digite a nova quantidade do item (deixe em branco se não quiser mudar): ")
        
        novo_preco = float(novo_preco) if novo_preco else None
        nova_quantidade = int(nova_quantidade) if nova_quantidade else None
        
        lista.atualizar(nome, novo_nome if novo_nome else None, novo_preco, nova_quantidade)
    elif opcao == "5":
        print("\033[32mPrograma encerrado.")  
        break
    else:
        print("\033[31mOpção Inválida. Tente novamente.")  