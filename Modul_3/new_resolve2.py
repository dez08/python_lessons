def send_email(message, recipient, sender='university.help@gmail.com'):
    for_test = ('.com', '.ru', '.net')
    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif not recipient.endswith(for_test) or not sender.endswith(for_test):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif recipient == sender:
        print('Невозможно оправить письмо самому себе.')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')