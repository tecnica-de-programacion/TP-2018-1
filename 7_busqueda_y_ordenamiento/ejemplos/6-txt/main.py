# Escritura
try:
    data_file = open('testfile.txt', 'w')
except FileNotFoundError:
    print('Error W testfile')
else:
    # data_file.write('Hello World')
    # data_file.write('This is our new text file')
    # data_file.write('and this is another line.')
    # data_file.write('Why? Because we can.')

    print('Hello World', file=data_file)
    print('This is our new text file', file=data_file)
    print('and this is another line.', file=data_file)
    print('Why? Because we can.', file=data_file)
    
    data_file.close() 

# Lectura
try:
    same_data_file = open('testfile.txt', 'r+')
except FileNotFoundError:
    print('Error R testfile')
else:
    print('File Name:', same_data_file.name)
    print('File Mode:', same_data_file.mode)
    print('File is Closed:', same_data_file.closed)

    print('Current ponter position : ', same_data_file.tell())
    same_data_file.seek(1, 0)
    print('Current ponter position : ', same_data_file.tell())
    inside_data = same_data_file.read(10)
    print('Inside file:', inside_data)

    same_data_file.seek(0, 0)
    print('Inside file:')
    for i,line in enumerate(same_data_file):
        print(i, line)
finally: 
    same_data_file.close()

# Cool
print('Cool')
try:
    with open('testfile.txt', 'r+') as data_in_file:
        for i, line in enumerate(data_in_file):
            print(i, line)
except FileNotFoundError:
    print('Error R testfile')

# Edición
import os
os.rename("testfile.txt", "test.txt")
os.remove("test.txt")

