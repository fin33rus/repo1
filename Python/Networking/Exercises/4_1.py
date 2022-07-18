nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
result = nat.replace("Fast", "Gigabit")
print(result)