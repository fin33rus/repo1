interface = input('Enter interface type and number: ')
vlan = input('Enter VLAN number: ')

access_template = ['  switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('\n' + '-' * 30)
print(f'interface {interface}')
print('\n  '.join(access_template).format(vlan))