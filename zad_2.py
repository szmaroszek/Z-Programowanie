class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f'Library in {self.city}, {self.zip_code}' +
                f'open hours: {self.open_hours}.')


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (f'Order date: {self.order_date}, Books:\n' +
                '\n'.join(str(book) for book in self.books) +
                f'\nOrdered by student - {self.student}' +
                f', processed by {self.employee} on {self.order_date}.' + '\n')


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f'Employee {self.first_name} {self.last_name}' +
                f', phone: {self.phone}.')


class Book():
    def __init__(self, library, publication_date,
                 author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f'Book from {self.library} Publication date ' +
                f'{self.publication_date} from {self.author_name}.')


library_1 = Library('Katowice', 'Hallera',
                    '50-211', '10:00 - 17:00', '868686868')
library_2 = Library('Katowice', 'Gospodarcza',
                    '50-215', '11:00 - 19:00', '686868686')

book_1 = Book(library_1, 2018, 'Rodney', 'Scott', 25)
book_2 = Book(library_1, 2017, 'Rodne', 'S', 250)
book_3 = Book(library_2, 2016, 'Rodn', 'Sc', 2500)
book_4 = Book(library_1, 2015, 'Rod', 'Sco', 25000)
book_5 = Book(library_2, 2014, 'Ro', 'Scot', 25000)

employee_1 = Employee('Szymon', 'Maroszek', 2019,
                      '21-08-2010', 'Katowice',
                      'Gospodarcza', '10-201', '999999999')
employee_2 = Employee('Szymon2', 'Maroszek3', 2020,
                      '22-09-2011', 'Sosnowiec',
                      'Hallera', '15-201', '999994999')
employee_3 = Employee('Szymon3', 'Maroszek3', 2021,
                      '23-09-2013', 'Radom', 'Galla',
                      '10-209', '999933999')

order_1 = Order(employee_1, True, [book_1, book_2], '22-10-2022')
order_2 = Order(employee_3, False, [book_4, book_3, book_5], '22-11-2022')

print(order_1)
print(order_2)
