from unittest import result


mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []

for i in mac:   
    result.append(i.replace(":", "."))
    print(result)