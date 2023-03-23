import random
def random_file_line_read(fname):
    lines=open(fname).read().splitlines()
    print(lines)
    return random.choice(lines)
print(random_file_line_read("test.txt"))



