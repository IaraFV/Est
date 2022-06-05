#eConnect - Sistema para provedores de Internet

from http.cookiejar import LoadError
import sqlite3
 
def inicializa_bd():
   con = sqlite3.connect("sis_clientes.db")
   cursor = con.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_de_clientes ( id integer not null, nome VARCHAR(100) not null, cpf VARCHAR(11) not null, email VARCHAR(100), codigo_do_plano integer, PRIMARY KEY (id));")
   cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_de_planos ( codigo integer not null, nome  VARCHAR(200) not null, valor integer not null, PRIMARY KEY (codigo));")
   con.commit()
   con.close()
   
def menu_de_opcoes(): 
   print(" 1. Cadastro de clientes")
   print(" 2. Cadastro de planos")
   print(" 3. Sair")

def menu(): 
   print(" 1. Cadastrar Novo Cliente")
   print(" 2. Listar Clientes")
   print(" 3. Editar Cliente")
   print(" 4. Remover Clientes")
   print(" 5. Sair")

def cadastro_de_clientes():
   con = sqlite3.connect("sis_clientes.db")
   cursor = con.cursor()
   print("=== CADASTRO DE CLIENTES ===")
   id= int(input("Id:"))
   nome = str(input("Nome:"))
   cpf = int(input("Cpf:"))
   email = str(input("Email:"))
   codigo_do_plano = int(input("Codigo do plano:"))
  
   consultaInsert = ("INSERT INTO cadastro_de_clientes (id,nome,cpf,email,codigo_do_plano) VALUES (?,?,?,?,?);")
   cursor.execute (consultaInsert,(id,nome,cpf,email,codigo_do_plano))
   con.commit()
   con.close()

def listar_cadastro_de_clientes(): 
   con = sqlite3.connect("sis_clientes.db")
   cursor = con.cursor()
   consulta = "SELECT id, nome, cpf, email, codigo_do_plano FROM cadastro_de_clientes;"
   cursor.execute(consulta)
   print("== Alunos cadastrados ==")
   for linha in cursor.fetchall():
       print("id", linha[0])
       print("Nome:", linha[1])
       print("cpf:", linha[2])
       print("email:", linha[3])
       print("codigo_do_plano:", linha[4])
       print(" -------------------")
   con.close()


def editar_cliente():
    listar_cadastro_de_clientes()
    con = sqlite3.connect("sis_clientes.db")
    cursor = con.cursor()
    id = int(input("Qual o id do cliente que deseja atualizar? "))
    coluna = str("nome")
    editar = str(input("para qual nome deseja alterar?"))
    consultaUpdate = "UPDATE cadastro_de_clientes SET "+coluna+ "=? WHERE id = ?;"
    cursor.execute(consultaUpdate,(editar,id))
    con.commit()
    con.close()
    print("atualizado")


#remover_clientes


def remover_clientes(): 
   id = int(input("Qual o id do cliente a remover?"))
   con = sqlite3.connect("sis_clientes.db")
   cursor = con.cursor()
   consultaDelete = "DELETE FROM cadastro_de_clientes WHERE id =?;"
   cursor.execute(consultaDelete,[(id)])
   con.commit()
   con.close()
   

def sair():
   print("AudioHandlers")

def opcao_invalida(): 
   print("Você digitou uma opção inválida")

#menu_planos


def menu_Planos():
   print(" 1. Cadastrar Novo Plano")
   print(" 2. Listar Planos")
   print(" 3. Editar Plano")
   print(" 4. Remover Planos")
   print(" 5. Voltar ao Menu Principal")


def cadastro_de_planos():
   con = sqlite3.connect("sis_clientes.db")
  
   cursor = con.cursor()
   print("=== CADASTRO DE PLANOS ===")
   codigo= int(input("Codigo:"))
   nome = input("Nome:")
   valor = input("Valor:")
  
   consultaInsert = "INSERT INTO cadastro_de_planos (codigo,nome,valor) VALUES (?,?,?);"
   cursor.execute(consultaInsert,(codigo,nome,valor))
   con.commit()
   con.close()
   

def listar_cadastro_de_planos():
   con = sqlite3.connect("sis_clientes.db")
   cursor = con.cursor()
   consulta = "SELECT codigo, nome, valor FROM cadastro_de_planos;"
   cursor.execute(consulta)
   print("== Cadastro de planos ==")
   for linha in cursor.fetchall():
       print("codigo", linha[0])
       print("Nome:", linha[1])
       print("valor:", linha[2])
       print(" -------------------")
   con.close()


def atualizar_cadastro_de_planos():
    listar_cadastro_de_planos()
    con = sqlite3.connect("sis_clientes.db")
    cursor = con.cursor()
    codigo = int(input("Qual o codigo do cliente que deseja atualizar? "))
    coluna = str("nome")
    editar = str(input("para qual nome deseja alterar?"))
    consultaUpdate = "UPDATE cadastro_de_planos SET "+coluna+ "=? WHERE codigo = ?;"
    cursor.execute(consultaUpdate,(editar,codigo))
    con.commit()
    con.close()

def sair():
   print("AudioHandlers")
 
def opcao_invalida():
   print("Você digitou uma opção inválida")

def remover_cadastro_de_planos():
   codigo = int(input("Qual o codigo do plano a remover? "))
   con = sqlite3.connect("sis_clientes.db")
   cursor = con.cursor()
   consultaDelete = "DELETE FROM cadastro_de_planos WHERE codigo =?;"
   cursor.execute(consultaDelete,[(codigo)])
   con.commit()
   con.close()
   

#Sistema de Cadastro de clientes
   
inicializa_bd()
opcao1 = 1
while (opcao1!=9):
    menu_de_opcoes()
    opcao = int(input("Opcao:"))
    if (opcao==1):  
        menu()
        opcao2 = int(input("Opção: "))
        if (opcao2==1):
           cadastro_de_clientes()
           print("DADOS SALVOS COM SUCESSO")
           menu_de_opcoes()
           opcao2 = input("Informe uma opção: ")
        if (opcao2 == 2):
           listar_cadastro_de_clientes()
           print("CLIENTES LISTADOS")
           menu_de_opcoes()
           opcao2 = input("Informe uma opção: ")
        if(opcao2==3):
           editar_cliente()
           print("DADOS EDITADOS COM SUCESSO")
           menu_de_opcoes()
           opcao2 = input("Informe uma opção: ")
        if(opcao2==4):
            remover_clientes()
            print("DADOS REMOVIDOS COM SUCESSO")
            menu_de_opcoes()
            opcao2 = input("Informe uma opção:")



    if (opcao==2):
      menu_Planos()
      opcao2 = int(input("Opcao2: "))
      if (opcao2==1):
         cadastro_de_planos()
         print("DADOS SALVOS COM SUCESSO")
      if (opcao2 == 2):
         listar_cadastro_de_planos()
         print("DADOS LISTADOS COM SUCESSO")
      if(opcao2==3):
         atualizar_cadastro_de_planos()
         print("DADOS ATUALIZADOS COM SUCESSO")
      if(opcao2==4):
         remover_cadastro_de_planos()
         print("DADOS REMOVIDOS COM SUCESSO")
                  
                
       
    if (opcao==3):
        sair()
        
    break
