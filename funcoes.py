import os

# Carregar txt
def load_txt():
    dados = {}

    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip().split(";")
            if len(linha) == 4:
                id, nome, preco, qtd = linha
                dados[id] = [nome, float (preco),int (qtd)]
    return dados


# Salvar txt
def salvar_txt (dados):
    with open (" dados.txt", "w") as arquivo:
        for id, info in dados.items():
            arquivo.write (f"{id}; {info[0]};{info[1]};{info[2]}\n")

# Cabeçalho
def cabecalho(titulo):
    print ("-"*50)
    print (titulo.center(50))
    print ("-"*50)

# Listar Produto
def listar (dados):
    cabecalho ("LISTA DE PRODUTOS")
    for id, info in dados.items():
        print (f"ID: {id} | Nome: {info[0]} | Preço: {info[1]:.2f} | Qtd: {info[2]}")
    print ("-"* 50)

# Pesquisar Produto
def pesquisar (dados):
    nome = input ("Digite o nome para pesquisar: ").lower()
    achou = False
    
    for id, info in dados.items():
        if nome in info [0].lower(): 
            print (f"ID: {id} | Nome: {info[0]} | Preço: {info[1]:.2f} | Qtd: {info[2]}")
            achou = True
    
    if not achou: 
        print ("Nenhum produto encontrado.")

# Incluir 
def incluir (dados):
    cabecalho ("INCLUIR PRODUTO")

    id = input ("ID do Produto: ")
    nome = input ("Nome: ")
    preco = float(input("Preço do Produto: "))
    qtd = int(input("Quantidade: "))

    dados[id] = [nome, preco, qtd]
    salvar_txt(dados)

# Alterar
def alterar(dados):
    cabecalho ("ALTERAÇÃO DO PRODUTO")
    id = input ("Digite o ID do Produto: ")
    if id not in dados:
        print ("Produto não encontrado!")
        return
    nome = input (f"Nome ( {dados[id][0]}): ") or dados[id][0]
    preco = input  (f"Preco ( {dados[id][1]}): ")
    qtd = input  (f"Quantidade ( {dados[id][2]}): ")

    dados[id] = [
        nome, 
        float(preco) if preco else dados[id][1],
        int (qtd) if qtd else dados[id][2],
    ]
    salvar_txt(dados)

# Excluir
def excluir (dados):
    cabecalho("EXCLUSÃO DE PRODUTO")
    id = input ("Digite o ID para excluir: ")
    
    if id in dados:
        del dados[id]
        salvar_txt[dados]
        print ("Produto Removido.")
    else:
        print ("ID não encontrado.")