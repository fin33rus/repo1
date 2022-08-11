import ipaddress

def convert_ranges_to_ip_list(ip_list):

    result_ip = []

    for ip in ip_list:
        if '-' in ip:
            start_ip, stop_ip = ip.split('-')
            if '.' not in stop_ip:
                stop_ip = '.'.join(start_ip.split('.'))[:-1] + stop_ip
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)

            for ip in range(int(start_ip), int(stop_ip) + 1):
                result_ip.append(str(ipaddress.ip_address(ip)))
        else:
            result_ip.append(ip)
    return result_ip

if __name__ == '__main__':
    my_result = convert_ranges_to_ip_list(
        ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
        )
    print(my_result)