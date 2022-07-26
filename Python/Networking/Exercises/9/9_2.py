trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = []
    for intf, vlan in intf_vlan_mapping.items():
        result.append(f'interface {intf}')
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                vlans_list = ','.join([str(vl) for vl in vlan])
                result.append(f'  {command} {vlans_list}')
            else:
                result.append(f'  {command}')
    return result

my_result = generate_trunk_config(trunk_config, trunk_mode_template)

for i in my_result:
    print(i)