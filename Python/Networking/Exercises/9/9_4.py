ignore = ["duplex", "alias", "configuration"]

def convert_config_to_dict(config_filename):
    config_dict = {}
    with open('config_sw1.txt') as config:
        for line in config:
            line = line.rstrip()
            if line and not line.startswith('!') or ignore_command(line, ignore):
                if line[0].isalnum():
                    command_key = line
                    config_dict[command_key] = []
                else:
                    config_dict[command_key].append(line.strip())
    return config_dict

def ignore_command(command, ignore):
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

my_result = convert_config_to_dict('config_sw1.txt')

for i, j in my_result.items():
    print(i, j)



