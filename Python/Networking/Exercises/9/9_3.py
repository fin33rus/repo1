def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename) as cfg:
        for line in cfg:
            line = line.rstrip()
            if line.startswith('interface'):
                intf = line.split()[1]
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                access_dict[intf] = vlan
            elif 'trunk allowed' in line:
                vlan_list = [int(v) for v in line.split()[-1].split(',')]
                trunk_dict[intf] = vlan_list
        return access_dict, trunk_dict

my_result = get_int_vlan_map('config_sw1.txt')

for i in my_result:
    for j in i:
        print(i, j)

# print(my_result)
