import csv
import operator

# Read Books
try:
    books_file = open('books.csv', 'r+', newline='')
    books = csv.reader(books_file)
    writer = csv.writer(books_file)
except FileNotFoundError:
    print('Error W testfile')
else:
    for book in books:
        print(book)
    books_file.seek(0, 0)
    for title, year, author in books:
        print(title, 'by', author, year)
    books_file.seek(0, 2)
    writer.writerow(('Sherlock Holmes', 1854, 'Arthur Conan Doyle'))
finally:
    books_file.close()

try:
    books_file = open('books.csv', 'a+', newline='')
    books_file.seek(0)
    fieldnames = ['Book', 'Year', 'Author']
    reader = csv.DictReader(books_file)
    writer = csv.DictWriter(books_file, fieldnames=fieldnames)
except FileNotFoundError:
    print('Error W testfile')
else:
    for row in reader:
        print('***' * 5)
        print(row)
        print('-' * 5)
        print(dict(row))
        print('***' * 5)
    books_file.seek(0, 2)
    writer.writerow({'Book': 'Don Quijote', 'Year': '1600', 'Author': 'Miguel de Cervantes'})
finally:
    books_file.close()
