result = '\n{:25} {}' * 5

with open('ospf.txt') as file:
    for line in file:
        line = line.replace(",", " ").replace("[", "").replace("]", "")
        line = line.split()
        print(result.format(
            'Prefix', line[1],
            'AD/Metric', line[2], 
            'Next-Hop', line[4],
            'Last update', line[5],
            'Outbound Interface', line[6]
        ))
                                                                                                                                                                                              
 