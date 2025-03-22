import sqlite3

def create_database():
    """
    Cria um banco de dados SQLite para armazenar dados financeiros.
    """
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY,
            ticker TEXT,
            date TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_data(ticker, date, price):
    """
    Salva dados de um ativo no banco de dados.
    """
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO stocks (ticker, date, price)
        VALUES (?, ?, ?)
    ''', (ticker, date, price))
    conn.commit()
    conn.close()