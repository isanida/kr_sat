import os

input = 'test'
output = 'test/cnf/sudoku'
sudoku_rules = open('./data/cnf/sudoku-rules.cnf', 'r').read()


def converter(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            size = 0
            l_equal = 0
            while l_equal != len(l):
                size += 1
                l_equal = size * size
            row = 0
            col = 1
            new_line = ''
            for idx, c in enumerate(l):
                if idx % size == 0:
                    row += 1
                    col = 1
                if c != '.':
                    new_line += '{}{}{} 0\n'.format(row, col, c)
                col += 1
            yield new_line, size



for root, subdirs, files in os.walk(input):
    for f in files:
        p = os.path.join(root, f)
        conv = converter(p)
        for idx, (c, size) in enumerate(conv):
            write_path = os.path.join(output, f)
            if not os.path.exists(write_path):
                os.mkdir(write_path)
            handle = open(os.path.join(write_path, str(idx) + '.txt'), 'w')
            appended = sudoku_rules + c
            handle.write(appended)
            handle.close()


