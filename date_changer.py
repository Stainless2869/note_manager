# Запрашиваем данные у пользователя
from time import process_time_ns

username     = input("Ведите имя пользователя: ")
title        = input("Ведите заголовок заметки: ")
content      = input("Введите описание заметки: ")
status       = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date   = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Преобразуем формат вывода даты (без года)
temp_issue_date   = issue_date [:-5] # Убираем год из строки
temp_created_date = created_date [:-5] # Убираем год из строки

# Вывод данных
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)