import uuid


class Book:
    def __init__(self, title, author, year, id=None, status='в наличии'):
        self.title = title
        self.author = author
        self.year = year
        self.id = id
        self.status = status

    def get_id(self):
        random_id = uuid.uuid4()
        self.id = random_id

    def __str__(self):
        return f'Книга -{self.title} , Автор - {self.author}, Год - {self.year}, Статус - {self.status}, id - {self.id}'


def save_json(obj_list):
    with open('data.json', 'w', encoding='utf-8') as f:
        for obj in obj_list:
            f.write(f'{obj.id},{obj.title},{obj.author},{obj.year},{obj.status} \n')


def load_json():
    data = []
    with open('data.json', 'r', encoding='utf-8') as f:
        for line in f:
            if line:
                l = line.replace(' \n', '').split(',')
                obj = Book(id=l[0], title=l[1], author=l[2], year=l[3], status=l[4])
                data.append(obj)
    if len(data) < 1:
        print('Библиотека пуста')
    return data


def create_book(title, author, year):
    book = Book(title, author, year)
    book.get_id()
    return book


def delete_book(data, id):
    obj_to_remove = None
    for obj in data:
        if obj.id == id:
            obj_to_remove = obj
    if obj_to_remove:
        data.remove(obj_to_remove)
    else:
        print('Книга не найдена')
    return data


def search_by_title(data, title):
    searching_obj = None
    for obj in data:
        if obj.title.lower() == title.lower():
            searching_obj = obj
            print(obj)
    if not searching_obj:
        print('Такой книги нет')


def search_by_author(data, author):
    searching_obj = None
    for obj in data:
        if obj.author.lower() == author.lower():
            searching_obj = obj
            print(obj)
    if not searching_obj:
        print('Такого автора нет')


def search_by_year(data, year):
    searching_obj = None
    for obj in data:
        if obj.year.lower() == year.lower():
            searching_obj = obj
            print(obj)
    if not searching_obj:
        print('Такого года нет')


def books_list(data):
    for obj in data:
        if obj:
            print(obj)
        else:
            print('Библиотека пуста')


def change_status(data, id):
    searching_obj = None
    for obj in data:
        if obj.id == id:
            searching_obj = obj
            if obj.status == 'в наличии':
                obj.status = 'выдана'
                print('Статус изменен')
            else:
                obj.status = 'в наличии'
                print('Статус изменен')
    if not searching_obj:
        print('Книга с таким id не найдена')
