vlan_num = input('Enter VLAN number: ')

with open('CAM_table.txt') as data:
    for line in data:
        words = line.split()
        if words and words[0].isdigit() and words[0] == vlan_num:
            vlan, mac, _, ports = words
            print(f"{vlan:9}{mac:20}{ports}")
            