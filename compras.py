import mysql.connector
import pandas as pd
from time import sleep

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="05102003",
    database="lista_de_compras"
)

mycursor = db.cursor()

while True:
    print(f'''\033[1m- - - - - Menu - - - - -\033[m
1 - Inserir
2 - Alterar
3 - Apresentar tabela por ordem de preço
4 - Deletar
5 - Sair''')
    print()
    pg = str(input('Qual é a sua escolha? '))
    print()
    if pg != '5':
        sql = 'select * from compras'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        frame = pd.read_sql("select * from compras", db, index_col='ID')
        print(frame)
        print()

    if pg == "1":
        while True:
            produto = str(input('Produto: ')).strip().capitalize()
            preço = float(input('Preço: '))
            quantidade = float(input('Quantidade: '))
            total = (preço * quantidade)
            sql = "INSERT INTO compras (Produtos, Preço, Quantidade, Total) " \
                  "VALUES(%s, %s, %s, %s)"
            cmd = (produto, preço, quantidade, total)
            mycursor.execute(sql, cmd)
            db.commit()
            resp = str(input("Já está? (S/N)")).strip().lower()
            if resp != "s" and resp != "n":
                resp = str(input("Já está? ")).strip().lower()
            if resp == "s":
                print()
                print('Aguarde...')
                sleep(3)
                print()
                print('Seus dados foram guardados com sucesso!')
                print()
                sql = 'select * from compras'
                mycursor.execute(sql)
                result = mycursor.fetchall()
                frame = pd.read_sql("select * from compras", db, index_col='ID')
                print(frame)
                sleep(3)
                print()
                break

    if pg == "2":
        while True:
            mudar = str(input("Alterar que coluna? ")).capitalize()
            pdt = str(input("Em qual produto?  (ID do produto)")).strip()
            md = str(input("Alterar para ...? "))
            sql = f"update compras set {mudar} = {md} " \
                  f"where ID = {pdt} "
            mycursor.execute(sql)
            db.commit()
            resp = str(input("Quer continuar a fazer alterações? (S/N)")).strip().lower()
            if resp != "s" and resp != "n":
                resp = str(input("Quer continuar a fazer alterações? ")).strip()
            if resp == "n":
                print()
                print('As suas alterações foram executados com sucesso! ')
                print()
                sql = 'select * from compras'
                mycursor.execute(sql)
                result = mycursor.fetchall()
                frame = pd.read_sql("select * from compras", db, index_col='ID')
                print(frame)
                print()
                sleep(2)
                break

    if pg == '3':
        while True:
            ordem = str(input("Por qual ordem de preço? [ASC/DESC] ")).strip().upper()
            if ordem != "DESC" and ordem != "ASC":
                ordem = str(input("Por qual ordem de preço? [ASC/DESC] ")).strip().upper()
            sql = f'select * from compras order by Preço {ordem}'
            mycursor.execute(sql)
            result = mycursor.fetchall()
            frame = pd.read_sql(f"select * from compras order by Preço {ordem}", db, index_col='ID')
            print(frame)
            sleep(2)
            break
    print()
    if pg == '4':
        while True:
            prd = str(input("Qual produto? (ID do produto) ")).strip().capitalize()
            if prd == "":
                prd = str(input("Qual produto? (ID do produto) ")).strip().capitalize()
            sql = f"delete from compras where ID = {prd}"
            mycursor.execute(sql)
            db.commit()
            while True:
                resp = str(input("Queres apagar mais algum produto? (S/N) ")).strip().lower()
                if resp != "s" and resp != "n":
                    res = str(input("Queres apagar mais algum produto? ")).strip().lower()
                if resp == "s":
                    prd = str(input("Qual produto? (ID do produto) ")).strip().capitalize()
                    if prd == "":
                        prd = str(input("Qual produto? (ID do produto) ")).strip().capitalize()
                    sql = f"delete from compras where ID = {prd}"
                    mycursor.execute(sql)
                    db.commit()
                else:
                    print(...)
                    sleep(2)
                    print("Seus dados foram apagados com sucesso!")
                    print()
                    sql = 'select * from compras'
                    mycursor.execute(sql)
                    result = mycursor.fetchall()
                    frame = pd.read_sql("select * from compras", db, index_col='ID')
                    print(frame)
                    print()
                    break

    if pg == '5':
        print()
        break
