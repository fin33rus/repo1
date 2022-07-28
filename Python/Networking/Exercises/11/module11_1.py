
def parse_cdp_neighbors(command_output):

    result = {}

    for line in command_output.split('\n'):
        line = line.strip()
        collumns = line.split()
        if '>' in line:
            hostname = line.split('>')[0]
        elif len(collumns) >= 5 and collumns[3].isdigit():
            r_dev, l_int, l_int_num, *others, r_int, r_int_num = collumns
            result[hostname, l_int + l_int_num] = (r_dev, r_int + r_int_num)
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))