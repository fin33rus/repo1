ip = "192.168.3.1"

octets = ip.split('.')
template = f"""
{octets[0]} {octets[1]:>10} {octets[1]:>10} {octets[1]:>10}
"""

print(template)