# Создание пустого словаря
note = {}

# Получения данных от пользователя
note["username"] = input('Введите имя пользователя: ').strip()

# Получение заголовков заметки от пользователя с размещением их в список внутри словаря
note["title"] = []
for i in range(3):
    title_temp = input(f'Введите {i+1} заголовок заметки: ').strip()
    note["title"].append(title_temp)

# Получение оставшихся данных о заметке от пользователя
note["content"] = input('Введите описание заметки: ').strip()
note["status"] = input('Введите статус заметки ("активна" или "завершена"): ').strip().lower()
note["created_date"] = input('Введите дату создания заметки в формате "ДД.ММ.ГГГГ": ')
note["issue_date"] = input('Введите дату истечения заметки в формате "ДД.ММ.ГГГГ": ')

# Создание словаря описания полей для вывода
note_print = {"username": "Имя пользователя",
              "title": "Заголовки заметки",
              "content": "Описание заметки",
              "status": "Статус заметки",
              "created_date": "Дата создания заметки",
              "issue_date": "Дата истечения заметки"
              }

# Блок вывода данных
for key, value in note.items():
    if key == "title":
        print(f'{note_print[key]}:', "; ".join(value))
    elif key == "created_date" or key == "issue_date":
        print(f'{note_print[key]}:', value[:5])
    else:
        print(f'{note_print[key]}: {value}')