import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")
    cur.execute("""INSERT INTO users (name, sex, old, score) VALUES ('Алексей', 1, 22, 1000)""")
    cur.execute("""INSERT INTO users (name, sex, old, score) VALUES ('Миша', 1, 19, 800)""")
    cur.execute("""INSERT INTO users (name, sex, old, score) VALUES ('Сергей', 1, 19, 900)""")
    cur.execute("""INSERT INTO users (name, sex, old, score) VALUES ('Мария', 2, 18, 1500)""")
    cur.execute("""INSERT INTO users (name, sex, old, score) VALUES ('Александр', 1, 20, 1100)""")
    cur.execute("""UPDATE users SET old = 20 WHERE old = 19""")
    cur.execute("""UPDATE users SET score = score + 300 WHERE score < 1000""")
    cur.execute("""UPDATE users SET score = score + 100 WHERE old >= 20""")
    cur.execute("""DELETE FROM users WHERE score < 1000""")

result = cur.execute("""SELECT name FROM users """).fetchall()
print("Все игроки из таблицы:", result)

result = cur.execute("""SELECT name FROM users WHERE sex = 2""").fetchall()
print("Игроки женского пола:", result)

result = cur.execute("""SELECT name FROM users WHERE score < 1000""").fetchall()
print("Игроки c результатом меньше 1000:", result)

result = cur.execute("""SELECT name FROM users ORDER BY score DESC""").fetchone()
print("Игрок с наилучшим результатом:", result)

result = cur.execute("""SELECT name FROM users WHERE old >= 18 AND old <= 20""").fetchall()
print("Игроки с возрастом 18-20 лет:", result)

cur.execute("""UPDATE users SET old = 20 WHERE old = 19""")
