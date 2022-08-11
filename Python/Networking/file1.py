import re

regex = r'(?P<mac>\S+) +(?P<address>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<intf>\S+)'
result = []

with open('dhcp_snooping.txt') as data:
    for line in data:
        match = re.search(regex, line)
        if match: 
            result.append(match.groupdict())

print(f'К свичу подключено {len(result)} устройств(а).')

for num, comp in enumerate(result, 1):
    print(f'Параметры устройства {num}: ')
    for key in comp:
        print(f' {key:10} : {comp[key]:10}')