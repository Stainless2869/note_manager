# Вспомнить Задание 4
# Запрашиваем информацию
username = input("Введите имя пользователя: ")
num_titles = int(input("Введите количество заголовков заметки: "))
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")


#Цикл добавления заголовков заметки
titles = []
for num in range(num_titles):
    title = input(f"Введите заголовок заметки {num + 1}: ")
    titles.append(title)

# Выводим данные заметки
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)

