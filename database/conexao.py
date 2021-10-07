import sqlite3

BASE_DADOS = 'database/database.db'

def conexao():
    conn = sqlite3.connect(BASE_DADOS)
    return conn