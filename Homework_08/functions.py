def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))

     
def delete_data(info: str) -> None:
    """Удаляет данные из справочника."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data):
        if info in contact:
            del data[i]
            with open('book.txt', 'w', encoding='utf-8') as file:
                file.writelines(data)
            print('Данные успешно удалены.')
            return
        else:
            print('Контакт не найден.')


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    results = []
    for contact in book:
        if info in contact:
            results.append(contact)
    if len(results) == 0:
        return 'Совпадений не найдено'
    if len(results) > 1:
        print('Найдено несколько совпадений. Выберите вариант из списка:')
        for i, contact in enumerate(results):
            print(f'{i+1}. {contact}')
        choice = input('> ')
        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(results):
            print('Некорректный ввод. Попробуйте еще раз.')
            choice = input('> ')
        return results[int(choice)-1]
    if len(results) == 1:
        return results[0]