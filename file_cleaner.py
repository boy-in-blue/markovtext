import string
import re

def clean(filein, fileout):
    with open(filein, 'r') as f:
        data = f.read()

    start_index = data.find('It is a')
    end_index = data.find('*** END')
    print(start_index, end_index)
    new_data = data[start_index:end_index]
    new_data = ''.join([i for i in new_data if i in string.printable])
    new_data = new_data.replace('\n', '')
    new_data = new_data.split(' ')
    new_data = ' '.join([i for i in new_data if i != ''])
    new_data = new_data.replace('_', '')
    for i in range(0, len(new_data), 1000):
        print(new_data[i:i+1000])
        if input() != '':
            break


    new_data = re.split(r'Chapter\s\d{1,2}', new_data)
    for i in new_data:
        print(i)
        if input() != '':
            break

    new_data = ''.join(new_data)

    with open(fileout, 'w') as f:
        f.write(new_data)

if __name__ == '__main__':
    clean('pride', 'pride_cleaned')
