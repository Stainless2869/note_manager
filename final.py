
# Храним Finaly

book = []

# Количество заметок
notes = int(input("\n Сколько заметок Вы хотите создать?: "))

# Создание и инициализация заметок
for i in range(notes):
    print(f"\nСоздание заметки {i + 1} из {notes}:\n")

    # Ввод пользователей
    num_users = int(input("Склько пользователей редактирует заметку?: "))
    users = [] # Внести в NOTE
    for n in range(num_users):
        tmp_user = input(f"Введите имя {n + 1}'го пользователя: ")
        users.append(tmp_user)

    # Ввод заметок
    num_title = int(input("Сколько заголовков будет в вашей Заметке?: "))
    titles = [] # Внести в NOTE
    for k in range(num_title):
        tmp_title = input(f"Введите название {k + 1}'го заголовка: ")
        titles.append(tmp_title)

    # Сама заметка по строкам
    print("Заметка 10 строк, пустые строки заполните 'Enter'")
    num_line = 10
    line = []
    for hop_line in range(num_line):
        tmp_line = input(f"{hop_line + 1}--> ")
        line.append(tmp_line)

    content     = line # Внести в NOTE

    status      = input("Введите статус заметки 'Активна/Выполнена: '")        # Внести в NOTE
    create_date = input("Введите дату создания заметки в формате 'д-м-г': ")   # Внести в NOTE
    issue_date  = input("Введите дату истечения заметки в формате 'д-м-г': ")  # Внести в NOTE

    tmp_cr_dt = create_date[:-5]
    tmp_is_dt = issue_date[:-5]

    # Созданная заметка в книгу
    note = {
        "users"  : users,
        "titles" : titles,
        "content": content,
        "status" : status,
        "create_date" : tmp_cr_dt,
        "issue_date" : tmp_is_dt,
    }

    book.append(note) #добавляем в конец списка заметок

# Просмотр заметок:
for index, note in enumerate(book, start = 1):  # index — порядковый номер заметки, note — текущая заметка в book = [{"key1": "value1"}, {"key2": "value2"}], то enumerate(1, {"key1": "value1"}), index = 1, note = {"key1": "value1"}
    print(f"\nЗаметка {index + 1}:  ") # В note сама заметка (note.items() вернет '['title','заголовок заметки']' этой заметки (key, value))
    for key, value in note.items(): # попадаем внутрь заметки, выделяем список
        if isinstance(value, list): # isinstance(объект, тип_данных) проверяет, является ли объект value экземпляром указанного типа
             print(f"{key.capitalize()}: ")
             for item in value: #выводим все списки (users, title. content)
                 print(f" - {item}") #(user_1. user_2)
        else:  # Если значение не список
            print(f"{key.capitalize()}: {value}")



