from componentes.rifa import Rifa
import database.conexao as db


def getRifas():
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


def getRifas(id):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM Rifas WHERE ID = ?;"
    cursor.execute(sql, [id])
    x = cursor.fetchall()[0]
    id = x[0]
    premio = x[1]
    qtd_num = x[2]
    status = x[3]
    rifa = Rifa(id, premio, qtd_num, status)
    conn.close()
    return rifa


def addRifa(rifa):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO Rifas (premio, qtd_num, status)VALUES (?,?,?);"
    cursor.execute(sql, [rifa.premio, rifa.qtd_num, rifa.status])
    conn.commit()
    conn.close()


def editRifa(rifa):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "UPDATE Rifas SET premio=?, qtd_num=?, status=? WHERE id=?"
    cursor.execute(sql, [rifa.premio, rifa.qtd_num, rifa.status, rifa.id])
    conn.commit()
    conn.close()


def delRifa(id):
    conn = db.conexao()
    cursor = conn.cursor()
    sql="DELETE FROM Rifas WHERE id=?"
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()