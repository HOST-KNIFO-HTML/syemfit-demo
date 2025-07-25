import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS clients (name TEXT, plan TEXT)')
c.executemany('INSERT INTO clients (name, plan) VALUES (?, ?)', [
    ('João', 'Mensal'),
    ('Maria', 'Trimestral'),
    ('Carlos', 'Semestral'),
    ('Ana', 'Anual'),
    ('Pedro', 'Mensal')
])
conn.commit()
conn.close()
print("✅ Banco populado com sucesso.")
