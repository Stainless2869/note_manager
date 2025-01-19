username     = input("Введитель пользователя заметки: ")

# Добавление Зоголовков
title_1 = input("Ведите 1й Заголовок Заметки: ")
title_2 = input("Ведите 2й Заголовок Заметки: ")
title_3 = input("Ведите 3й Заголовок Заметки: ")

title   = [title_1, title_2, title_3]

content      = input("Заполните заметку: ")
status       = input("Введите статус заметки")
created_date = input("Дата начала в формате 'д-м-г': ")
issue_date   = input("Дата истечения в формате 'д-м-г': ")


# Вывод результата
print("\n Вы ввели:")
print("Имя пользователя", username)
print("Введите Заголовки заметки", title)
print("Заполните заметку", content)
print("Статус заметки", status)
print("Дата создания Заметки", created_date[:-5])
print("Дата истечения заметки", issue_date[:-5])
