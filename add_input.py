# Получение данных о заметке от пользователя
username = input('Введите имя пользователя: ').strip()
title = input('Введите заголовок заметки: ').strip()
content = input('Введите описание заметки: ').strip()
status = input('Введите статус заметки ("активна" или "завершена"): ').strip().lower()
created_date = input('Введите дату создания заметки в формате "ДД.ММ.ГГГГ" (например 25.12.2024): ').strip()
issue_date = input('Введите дату истечения заметки в формате "ДД.ММ.ГГГГ" (например 25.12.2024): ').strip()

# Блок вывода данных
print('Имя пользователя: ', username)
print('Заголовок заметки: ', title)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date[:5])
print('Дата истечения заметки: ', issue_date[:5])