def read_otvet_lines():
    f = open('Otvet.txt', encoding='utf-8')
    lines = f.readlines()
    f.close()
    return lines

def get_random_otvet_line():
    from random import choice
    lines = read_otvet_lines()
    line = choice(lines)
    line = line.strip('\n')

    return line

def generate_random_ip():
    from random import randint
    
    return f'IP-{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}'