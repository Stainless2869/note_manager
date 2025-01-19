# Запрашиваем данные у пользователя
username     = input("Введите имя пользователя: ")
title        = input("Введите заголовок заметки: ")
content      = input("Заполните заметку: ")
status       = input("Введите статус заметки (Активна/Выполнена): ")
created_date = input("Введите дату создания заметки в формате 'д-м-г': ")
issue_date   = input("Введите дату окончания заметки в формате 'д-м-г': ")

#Исключаем год используя срез
tmp_cr_dt    = created_date [:-5]
tmp_iss_dt   = issue_date [:-5]

#Вывод результатов
print("\nВы ввели: ")
print("Пользователь: ", username)
print("Заголовк: ", title)
print("Содержание: ", content)
print("Статус: ", status)
print("Дата создания: ", tmp_cr_dt)
print("Дата истечения: ", tmp_iss_dt)

