config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config = config.split()
result = config[-1].split(',')
print(result)