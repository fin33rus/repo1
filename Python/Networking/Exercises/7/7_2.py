with open('config_sw1.txt') as data:
    for line in data:
        line = line.strip()
        if line.startswith('!'):
            continue
        else:
            print(line)