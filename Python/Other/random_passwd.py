import random


def generate_password(l,mode):
    ucode = (
        list(range(48,58)),
        list(range(65,91)),
        list(range(97,123)),
        list(range(33,48)) + list(range(58,65)) + list(range(91,97)) + list(range(123,127))
    )
    
    passwd = []
    combination = 0
    complexity = 'Отсутствует'
    
    while len(passwd) < l:
        match mode:
            case 1:
                passwd.append(chr(random.choice(ucode[0])))
                combination = 10 ** l
                if 0 < combination <= 100000000000:
                    complexity = 'Слабый пароль'
                else:
                    complexity = 'Средний пароль'
            case 2:
                passwd.append(chr(random.choice(ucode[1])))
                combination = 26 ** l
                if 0 < combination <= 208827064576:
                    complexity = 'Слабый пароль'
                elif 208827064576 < combination <= 2481152873203736576:
                    complexity = 'Средний пароль'
                elif 2481152873203736576 < combination <= 1133827315385150725554176:
                    complexity = 'Сильный пароль'
                else:
                    complexity = 'Очень сильный пароль'
            case 3:
                passwd.append(chr(random.choice(ucode[random.randint(1,2)])))
                combination = 52 ** l
                if 0 < combination <= 19770609664:
                    complexity = 'Слабый пароль'
                elif 19770609664 < combination <= 7516865509350965248:
                    complexity = 'Средний пароль'
                elif 7516865509350965248 < combination <= 1056931425538820521590784:
                    complexity = 'Сильный пароль'
                elif 1056931425538820521590784 < combination <= 148613013882162475899836956672:
                    complexity = 'Очень сильный пароль'
                else:
                    complexity = 'Невозможно взломать'
            case 4:
                passwd.append(chr(random.choice(ucode[random.randint(0,2)])))
                combination = 62 ** l
                if 0 < combination <= 56800235584:
                    complexity = 'Слабый пароль'
                elif 56800235584 < combination <= 839299365868340224:
                    complexity = 'Средний пароль'
                elif 839299365868340224 < combination <= 200028539268669788905472:
                    complexity = 'Сильный пароль'
                elif 200028539268669788905472 < combination <= 47672401706823533450263330816:
                    complexity = 'Очень сильный пароль'
                else:
                    complexity = 'Невозможно взломать'
            case 5:
                passwd.append(chr(random.choice(ucode[random.randint(0,3)])))
                combination = 94 ** l
                if 0 < combination <= 689869781056:
                    complexity = 'Слабый пароль'
                elif 689869781056 < combination <= 53861511409489970176:
                    complexity = 'Средний пароль'
                elif 53861511409489970176 < combination <= 475920314814253376475136:
                    complexity = 'Сильный пароль'
                elif 475920314814253376475136 < combination <= 395291798759681826446224359424:
                    complexity = 'Очень сильный пароль'
                else:
                    complexity = 'Невозможно взломать'
            case _:
                return 'Недопустимое значение'
    
    return ''.join(passwd), 'Надежность пароля: {0}'.format(complexity), 'Возможное количество комбинаций: {0}'.format(combination)


l = input('''
----------------------------------------------------------------
| Это мой личный рандомайзер паролей                           |
| Рекомендуется использовать пароль длиной от 4 до 18 символов |
| Введите длину пароля ниже:                                   |
----------------------------------------------------------------
\n''')

mode = input('''
-------------------------------------------------------------------------------------------------------
| А теперь выберите какие символы могут быть включены в созданный пароль(введите номер с клавиатуры): |
| 1. Только цифры (небезопасный способ)                                                               |
| 2. Только латинские строчные буквы                                                                  |
| 3. Латинские заглавные и строчные буквы                                                             |
| 4. Цифры, латинские заглавные и строчные буквы                                                      |
| 5. Цифры, латинские заглавные и строчные буквы + символы (предпочтительный способ)                  |
-------------------------------------------------------------------------------------------------------
\n''')
print()
print(generate_password(int(l),int(mode)))





