name = str(input('Введите имя: '))
age = int(input('Введите возрас: '))

rez_text = ''
if not name:
    rez_text += 'Ошибка: пустое имя.'
elif len(name) < 3:
    rez_text += 'Ошибка: В имени должно быть минимум 3 символа.'
elif age <= 0:
    rez_text += 'Ошибка: возраст не можеть быть равен или меньше 0'
elif age < 14:
    rez_text += 'Ошибка: Минимальный возраст — 14 лет.'
elif not rez_text:
    rez_text += f'Привет,{name.title()}! Тебе {age} лет.'
    if 16 <= age <= 17:
        rez_text += 'Нужно не забыть получить первый паспорт'
    elif 25 <= age <= 26:
        rez_text += 'Не забудь заменить паспорт по достижению 25 лет.'
    elif 45 <= age <= 46:
        rez_text += 'Не забудь заменить паспорт по достижению 45 лет.'


print(rez_text)
