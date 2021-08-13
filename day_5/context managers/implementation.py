from contextlib import contextmanager


@contextmanager
def read_file(file_name):
    f = open(file_name, 'rb')

    line_count = 0
    for line in f:
        line_count += 1
    print(line_count)

    yield f
    f.close()


with read_file('test_file.txt') as f:
    print('Файл открыт')

