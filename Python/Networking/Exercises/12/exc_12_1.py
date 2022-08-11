from os import devnull
import subprocess

def ping_ip_addresses(ip_list):
    available_ip = [] 
    unavailable_ip = []

    for ip in ip_list:
        result = subprocess.run(
            ['ping', '-c',  '1', ip],
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL       
            )
        if result.returncode == 0:
            available_ip.append(ip)
        else:
            unavailable_ip.append(ip)
    return available_ip, unavailable_ip


if __name__ == '__main__':
    my_ips = ping_ip_addresses(['8.8.8.8', '192.168.1.60', '8.8.4.4', '192.168.1.70'])

    for good, bad in my_ips:
        print(good, bad)