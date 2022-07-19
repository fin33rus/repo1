ignore = ["duplex", "alias", "configuration"]

with open('config_sw1.txt') as data:
    for line in data:
        lines = line.split()
        lines_intersect = set(lines) & set(ignore)
        if not line.startswith('!') and not lines_intersect:
            print(line.rstrip())
