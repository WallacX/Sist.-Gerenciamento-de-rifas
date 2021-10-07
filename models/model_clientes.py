from componentes.cliente import Cliente
import database.conexao as db

def getClientes():
    conn = db.conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes;")
    lista_clientes = []

    for x in cursor.fetchall():
        id = x[0]
        nome = x[1]
        cpf = x[2]
        telefone = x[3]
        email = x[4]
        cliente = Cliente(id, nome, cpf, telefone, email)
        lista_clientes.append(cliente)
    conn.close()
    return lista_clientes


def getCliente(id):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM Clientes WHERE ID = ?;"
    cursor.execute(sql, [id])
    x = cursor.fetchall()[0]
    id = x[0]
    nome = x[1]
    cpf = x[2]
    telefone = x[3]
    email = x[4]
    cliente = Cliente(id, nome, cpf, telefone, email)
    conn.close()
    return cliente


def addCliente(cliente):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO Clientes (nome,cpf,telefone,email)VALUES (?,?,?,?);"
    cursor.execute(sql, [cliente.nome, cliente.cpf,cliente.telefone, cliente.email])
    conn.commit()
    conn.close()


def editCliente(cliente):
    conn = db.conexao()
    cursor = conn.cursor()
    sql = "UPDATE Clientes SET nome=?, cpf=?, telefone=?, email=? WHERE id=?"
    cursor.execute(sql,[cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.id])
    conn.commit()
    conn.close()


def delCliente(id):
    conn = db.conexao()
    cursor = conn.cursor()
    sql="DELETE FROM Clientes WHERE id=?"
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()
    

