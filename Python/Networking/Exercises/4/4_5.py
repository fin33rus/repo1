command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command1 = command1.split()
command1 = command1[-1].split(",")

command2 = command2.split()
command2 = command2[-1].split(",")

result = set(command1) & set(command2)

print(result)