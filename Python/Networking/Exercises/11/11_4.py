from module11_2 import create_network_map
from module11_3 import unique_network_map
from draw_network_graph import draw_topology

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]


if __name__ == '__main__':
    topology = create_network_map(infiles)
    result = unique_network_map(topology)
    draw_topology(result, 'img1')
    print(result)
