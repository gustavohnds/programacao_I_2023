import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='atvcrud')

#print("Funcionou a conexão")
cursor = conexao.cursor()  # executar a conexão

#menu
while True:
    print("O que deseja realizar?")
    print("----------------")
    print("1 - Incluir item")
    print("2 - Listar item")
    print("3 - Atualizar item")
    print("4 - Deletar item")
    print("----------------")
    op = int(input("Digite a opção desejada:"))

    #selecionar opcao
    # 1 - incluir item 
    if op == 1:
        produto = input("Digite o nome do item: ")
        valor = float(input("Digite o valor do item: "))
        comando = f'INSERT INTO VENDAS(nome_produto, valor) VALUES ("{produto}", {valor})'
        cursor.execute(comando)
        conexao.commit()
        #resultado = cursor.fetchall() 
        #print(resultado)
        print("Item incluído!")

    #2 - listar
    elif op == 2:
        comando = f'SELECT * FROM VENDAS'
        cursor.execute(comando)
        #conexao.commit() #-> edita o banco de dados
        resultado = cursor.fetchall()  # --> ler o banco de dados
        print(resultado)

    #3 - editar valor item
    elif op == 3:
        nome_produto = input("Digite o nome do produto:")
        valor = float(input("Digite o novo valor:"))
        comando = f'UPDATE VENDAS SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit() #-> edita o banco de dados
        resultado = cursor.fetchall()  # --> ler o banco de dados
        print(resultado, "Item editado!")

    #4 - deletar item
    elif op == 4:
        nome_produto = input("Digite o nome do produto que deseja deletar:")
        comando = f'DELETE FROM VENDAS WHERE nome_produto = "{nome_produto}"'
        cursor.execute(comando)
        conexao.commit() #-> edita o banco de dados
        resultado = cursor.fetchall()  # --> ler o banco de dados
        print(resultado,"Item excluído!")

    op3 = input("Deseja fazer mais alguma coisa? (s/n): \n" )
    if op3 == 'n':
        break
        
cursor.close()
conexao.close()
