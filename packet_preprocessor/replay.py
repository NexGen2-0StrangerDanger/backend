from scapy.all import *
from tqdm import tqdm

# pbar = tqdm(total=1300000)

ip_map = {"192.168.2.15": "172.17.0.2",
          "192.168.100.5": "172.17.0.3", "192.168.2.13": "172.17.0.1"}
for i, p in enumerate(PcapReader("ARP_MitM_pcap.pcapng")):
    # pbar.update(1)
    # if i < 1300000:
    #     continue
    # pbar.close()
    # if IP not in p:
    #     continue
    # p = p[IP]
    # # if you want to use a constant map, only let the following line
    # p.src = "172.17.0.3"
    # p.dst = "172.17.0.2"
    # if you want to use the original src/dst if you don't find it in ip_map
    p.src = ip_map.get(p.src, p.src)
    p.dst = ip_map.get(p.dst, p.dst)
    # if you want to drop the packet if you don't find both src and dst in ip_map
    # if p.src not in ip_map or p.dst not in ip_map:
    #     continue
    # p.src = ip_map[p.src]
    # p.dst = ip_map[p.dst]
    # as suggested by @AliA, we need to let Scapy compute the correct checksum
    # del (p.chksum)
    # then send the packet
    send(p)
