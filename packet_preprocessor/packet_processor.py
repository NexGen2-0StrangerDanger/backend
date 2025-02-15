from FeatureExtractor import FE
import netStat as ns
import numpy as np


maxHost = 100000000000
maxSess = 100000000000


def process_packets(packets, nstat=ns.netStat(np.nan, maxHost, maxSess)):
    vectors = []
    for packet in packets:
        IPtype = np.nan
        timestamp = packet[0]
        framelen = packet[1]
        srcIP = ''
        dstIP = ''
        if packet[4] != '':  # IPv4
            srcIP = packet[4]
            dstIP = packet[5]
            IPtype = 0
        elif packet[17] != '':  # ipv6
            srcIP = packet[17]
            dstIP = packet[18]
            IPtype = 1
        srcproto = packet[6] + packet[8]
        dstproto = packet[7] + packet[9]  # UDP or TCP port
        srcMAC = packet[2]
        dstMAC = packet[3]
        if srcproto == '':  # it's a L2/L1 level protocol
            if packet[12] != '':  # is ARP
                srcproto = 'arp'
                dstproto = 'arp'
                srcIP = packet[14]  # src IP (ARP)
                dstIP = packet[16]  # dst IP (ARP)
                IPtype = 0
            elif packet[10] != '':  # is ICMP
                srcproto = 'icmp'
                dstproto = 'icmp'
                IPtype = 0
            elif srcIP + srcproto + dstIP + dstproto == '':  # some other protocol
                srcIP = packet[2]  # src MAC
                dstIP = packet[3]
        print([IPtype, srcMAC, dstMAC, srcIP, srcproto, dstIP,
              dstproto, int(framelen), float(timestamp)])
        vector = nstat.updateGetStats(
            IPtype, srcMAC, dstMAC, srcIP, srcproto, dstIP, dstproto,
            int(framelen), float(timestamp))
        vectors.append(vector)
    return np.array(vectors)
