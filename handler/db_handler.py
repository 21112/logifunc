import sqlite3

conn = sqlite3.connect('handler/users.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY AUTOINCREMENT,name TEXT, password TEXT);')
conn.commit()
#cur.execute('INSERT INTO users(name,password) VALUES ("admin", "admin");')

#cur.execute('UPDATE users SET name = "Admin" WHERE name = "admin";')
conn.commit()
cur. execute('SELECT * FROM users;')
f = cur.fetchall()
print(f)


def login(login,passw, signal):
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()
    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name = "{login}";')
    value = cur.fetchall()
    if value !=[] and value[0][2] == passw:
        signal.emit('Gradulation! Autorisition!')
        
    else:
        signal.emit('Error!')

def register(login, passw, signal):
    con = sqlite3.connect('handler/users.db')
    cur = con.cursor()
    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name = "{login}";')
    value = cur.fetchall()
    if value !=[]:
        signal.emit('Nikname is using')

        
    elif value == []:

        cur.execute('INSERT INTO users (name, password) VALUES ("{login}", "{passw}");')
        signal.emit("Registration!")
        con.commit()
    cur.close()
    con.close()

