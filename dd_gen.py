import random
import string
import pyperclip
n = int(input('How many lines to generate? (DEFAULT=10)') or "10")
TABLE_NAME = input('Table name: ')
data = input('Input data: ')
output = ''
for i in range(n):
    arr = data.split(',')
    attributes = []
    values = []
    query = 'INSERT INTO {}('.format(TABLE_NAME)
    for index, item in enumerate(arr):
        arr[index] = (item.strip().split()[0], item.strip().split()[1])
        attributes.append(arr[index][0])
    attributes = ", ".join(attributes)
    query += attributes
    query += ') VALUES('
    for item in arr:
        if(item[1] == 'int'):
            values.append(str(random.randint(1,100)))
        elif(item[1] == 'float'):
            values.append(str(round(random.random() * random.randint(1,99), 2)))
        elif(item[1] == 'varchar'):
            values.append(f"'{''.join(random.choices(string.ascii_lowercase, k=random.randint(5,10)))}'")
    values = ", ".join(values)
    query += values + ');'
    print(query)
    output += '{}\n'.format(query)
pyperclip.copy(output)
