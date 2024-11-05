import sqlite3
from datetime import datetime

conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def add_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    print("Заметка добавлена.")

def view_notes():
    cursor.execute("SELECT id, title, created_at FROM notes")
    notes = cursor.fetchall()
    if notes:
        print("\nВсе заметки:")
        for note in notes:
            print(f"ID: {note[0]}, Заголовок: {note[1]}, Дата создания: {note[2]}")
    else:
        print("Заметок пока нет.")

def edit_note():
    note_id = input("Введите ID заметки, которую хотите отредактировать: ")
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    note = cursor.fetchone()
    if note:
        new_title = input(f"Текущий заголовок ({note[1]}). Введите новый заголовок: ") or note[1]
        new_content = input(f"Текущее содержание ({note[2]}). Введите новое содержание: ") or note[2]
        cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (new_title, new_content, note_id))
        conn.commit()
        print("Заметка обновлена.")
    else:
        print("Заметка с таким ID не найдена.")

def delete_note():
    note_id = input("Введите ID заметки, которую хотите удалить: ")
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    print("Заметка удалена.")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Посмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")



if __name__ == "__main__":
    main()

conn.close()
