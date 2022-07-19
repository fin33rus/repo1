vlan_num = input('Enter VLAN number: ')
mac_table = []

with open('CAM_table.txt') as data:
    for line in data:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, ports = words
            mac_table.append([int(vlan), mac, ports])
            
for vlan, mac, ports in mac_table:
    print(f'{vlan:<9}{mac:20}{ports}')