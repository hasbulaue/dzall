import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT,
    gpa REAL
)
''')

students = [
    ('Иван Иванов', 20, 'Информатика', 4.5),
    ('Мария Петрова', 21, 'Математика', 4.8),
    ('Алексей Сидоров', 19, 'Физика', 4.2),
    ('Елена Кузнецова', 22, 'Химия', 4.7),
    ('Дмитрий Смирнов', 20, 'Биология', 4.3)
]

cursor.executemany('INSERT INTO students (name, age, major, gpa) VALUES (?, ?, ?, ?)', students)

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

conn.close()