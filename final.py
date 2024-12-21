# Заполнение Заметки
note = {}
note["username"] = input("Введите имя пользователя: ")
note["num_titles"] = int(input("Введите количество заголовков заметки: "))
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")


# Инициализация Заголовка заметки
note["titles"] = []
for i in range(note["num_titles"]):
    title = input(f"Введите заголовок {i + 1}: ")
    note["titles"].append(title)

# Выыод
for key, value in note.items():
    print(f"{key.capitalize()} : {value}")
