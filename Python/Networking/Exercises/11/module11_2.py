from module11_1 import parse_cdp_neighbors

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

network_map = {}

def create_network_map(filenames):
    for files in filenames:
        with(open(files)) as data:
            parsed = parse_cdp_neighbors(data.read())
            network_map.update(parsed)
    return network_map


if __name__ == "__main__":
    topology = create_network_map(infiles)
    print(topology)