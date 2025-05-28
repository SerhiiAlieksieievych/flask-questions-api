import sqlite3

questions = [
    ("Яка столиця Франції?", "Берлін", "Париж", "Рим", "Мадрид", "Париж"),
    ("Скільки континентів на Землі?", "5", "6", "7", "8", "7"),
    ("Який найбільший океан?", "Атлантичний", "Індійський", "Північний Льодовитий", "Тихий", "Тихий")
]

conn = sqlite3.connect('questions.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        answer TEXT NOT NULL
    )
''')

c.execute('DELETE FROM questions')

c.executemany('''
    INSERT INTO questions (question, option_a, option_b, option_c, option_d, answer)
    VALUES (?, ?, ?, ?, ?, ?)
''', questions)

conn.commit()
conn.close()
print("Базу даних ініціалізовано.")
