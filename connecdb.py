# connect_db.py
import sqlite3
class Connect(object):
def __init__(self, db_name):
    try:
        # abrindo conex�o...
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        # imprimindo nome do banco
        print("Banco:", db_name)
        # lendo a vers�o do SQLite
        self.cursor.execute('SELECT SQLITE_VERSION()')
        self.data = self.cursor.fetchone()
        # imprimindo a vers�o do SQLite
        print("SQLite version: %s" % self.data)
    except sqlite3.Error:
        print("Erro ao abrir banco.")
        return False

class ClientesDb(object):
    def __init__(self):
        self.db = Connect('clientes.db')
    def close_connection(self):
        self.db.close_db()

if __name__ == '__main__':
    cliente = ClientesDb()
    cliente.close_connection()
