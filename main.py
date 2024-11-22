from func import load_json, create_book, save_json, delete_book, search_by_title, search_by_author, search_by_year, \
    books_list, change_status

session = True
data = load_json()

while session:

    choice = input('Вы находитесь в главном меню библиотеки \n'
                   'Выберите интересующий вас раздел: \n'
                   '1. - Добавить книгу \n'
                   '2. - Удалить книгу \n'
                   '3. - Поиск по названию\n'
                   '4. - Поиск по автору\n'
                   '5. - Поиск по году\n'
                   '6. - Список книг\n'
                   '7. - Изменить статус книги\n'
                   '8. - Завершить сеанс\n')

    if choice == '1':
        title, author, year = input('Введите название книги: '), input('Введите имя автора: '), input(
            'Введите год изданя: ')
        book = create_book(title, author, year)
        data.append(book)
        input('Нажмите клавишу Enter для возврата в главное меню')

    elif choice == '2':
        id = input('Введите id книги для удаления \n')
        delete_book(data, id)
        input('Нажмите клавишу Enter для возврата в главное меню')

    elif choice == '3':
        title = input('Введите название книги для поиска \n')
        search_by_title(data, title)
        input('Нажмите клавишу Enter для возврата в главное меню')

    elif choice == '4':
        author = input('Введите автора книги для поиска \n')
        search_by_author(data, author)
        input('Нажмите клавишу Enter для возврата в главное меню')

    elif choice == '5':
        year = input('Введите год книги для поиска \n')
        search_by_year(data, year)
        input('Нажмите клавишу Enter для возврата в главное меню')

    elif choice == '6':
        books_list(data)
        input('Нажмите клавишу Enter для возврата в главное меню')

    elif choice == '7':
        id = input('Введите id книги для изменения статуса \n')
        change_status(data, id)
        input('Нажмите клавишу Enter для возврата в главное меню')

    elif choice == '8':
        save_json(data)
        session = False

    else:
        print('Введите корректный номер раздела')
        input('Нажмите клавишу Enter для возврата в главное меню')
