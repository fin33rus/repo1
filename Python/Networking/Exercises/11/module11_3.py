from module11_2 import create_network_map

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def unique_network_map(topology_dict):

    network_map = {}

    for key, value in topology_dict.items():
        if not network_map.get(value) == key:
            network_map[key] = value
    
    return network_map

if __name__ == '__main__':

    topology = create_network_map(infiles)
    result_topology = unique_network_map(topology)
    
    for i, j in result_topology.items():
        print(i , j)