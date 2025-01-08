phone_book = {
    'Руслан': ('+995595507248', '89024429634'),
    'Петя': '88005553535',
    'Вася': '88005553531'
}

for contact in phone_book:
    number = phone_book[contact]
    print(f'{contact}: {number}')
