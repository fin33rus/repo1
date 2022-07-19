result = {}

with open('sh_ip_int.txt') as file:
    for line in file:
        if 'line protocol' in line:
            interface = line.split()[0]
        elif 'MTU is' in line:
            mtu = line.split()[-2]
            result[interface] = mtu

for i, j in result.items():
    print(i, j)