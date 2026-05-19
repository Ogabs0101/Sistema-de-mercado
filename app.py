import os
os.system ('cls')
import funcoes as fc

def menu ():
    print ("\n" + "-" * 50)
    print ("SISTEMA DE CONTROLE DE VENDAS".center(50))
    print ("-" * 50)
    print ('''
    [1] Pesquisa por Produto
    [2] Listar Todos
    [3] Incluir Novo Produto
    [4] Alterar Produto
    [5] Excluir Produto
    [S] Sair
''')
    print ("-" * 50)
def main():
    dados = fc.load_txt()
    while True:
        menu()
        op = input("Escolha: ").upper()

        if op == "1":
            fc.pesquisar(dados)
        elif op == "2":
            fc.listar(dados)
        elif op == "3":
            fc.incluir(dados)
        elif op == "4":
            fc.alterar(dados)
        elif op == "5":
            fc.excluir(dados)
        elif op == "S":
            break
            print ("Opção inválidada!")
        input ("\nPressione ENTER para continuar...")
        os.system ("cls" if os.name == "nt" else "clear")
if __name__ == "__main__":
    main()


