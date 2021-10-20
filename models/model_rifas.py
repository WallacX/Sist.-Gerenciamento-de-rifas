from componentes.rifa import Rifa
import database.conexao as db


def addRifa(rifa):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO Rifas (premio, qtd_num, status)VALUES (?,?,?);"
    cursor.execute(sql, [rifa.premio, rifa.qtd_num, rifa.status])
    conn.commit()
    conn.close()


def FinalizaRifa(rifa):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "UPDATE Rifas SET premio=?, qtd_num=?, status='FINALIZADA' WHERE id=?"
    cursor.execute(sql, [rifa.premio, rifa.qtd_num, rifa.status, rifa.id])
    conn.commit()
    conn.close()


def getAtivas():
    conn = db.conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Rifas WHERE status = 'ATIVA';")
    lista_rifas = []

    for x in cursor.fetchall():
        premio = x[1]
        lista_rifas.append(premio)
    conn.close()
    return lista_rifas


def getRifa(premio):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM Rifas WHERE premio = ?;"
    cursor.execute(sql, [premio])
    x = cursor.fetchall()[0]
    id = x[0]
    premio = x[1]
    qtd_num = x[2]
    status = x[3]
    rifa = Rifa(id, premio, qtd_num, status)
    conn.close()
    return rifa




'''def getRifas():
    conn = db.conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Rifas;")
    lista_rifas = []

    for x in cursor.fetchall():
        id = x[0]
        premio = x[1]
        qtd_num = x[2]
        status = x[3]
        rifa = Rifa(id, premio, qtd_num, status)
        lista_rifas.append(rifa)
    conn.close()
    return lista_rifas
def delRifa(id):
    conn = db.conexao()
    cursor = conn.cursor()
    sql="DELETE FROM Rifas WHERE id=?"
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()'''