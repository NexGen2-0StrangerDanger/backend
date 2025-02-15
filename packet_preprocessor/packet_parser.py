def parse_packet(raw_packet):
    time_epoch = raw_packet.frame_info.time_epoch
    frame_len = raw_packet.frame_info.len
    eth_src = raw_packet.eth.src
    eth_dst = raw_packet.eth.dst
    if hasattr(raw_packet, 'ip'):
        ip_src = raw_packet.ip.src
        ip_dst = raw_packet.ip.dst
    else:
        ip_src = ""
        ip_dst = ""
    if hasattr(raw_packet, 'tcp'):
        tcp_srcport = raw_packet.tcp.srcport
        tcp_dstport = raw_packet.tcp.dstport
    else:
        tcp_srcport = ""
        tcp_dstport = ""
    if hasattr(raw_packet, 'udp'):
        udp_srcport = raw_packet.udp.srcport
        udp_dstport = raw_packet.udp.dstport
    else:
        udp_srcport = ""
        udp_dstport = ""
    if hasattr(raw_packet, 'icmp'):
        icmp_type = raw_packet.icmp.type
        icmp_code = raw_packet.icmp.code
    else:
        icmp_type = ""
        icmp_code = ""
    if hasattr(raw_packet, "arp"):
        arp_opcode = raw_packet.arp.opcode
        arp_src_hw_mac = raw_packet.arp.src_hw_mac
        arp_src_proto_ipv4 = raw_packet.arp.src_proto_ipv4
        arp_dst_hw_mac = raw_packet.arp.dst_hw_mac
        arp_dst_proto_ipv4 = raw_packet.arp.dst_proto_ipv4
    else:
        arp_opcode = ""
        arp_src_hw_mac = ""
        arp_src_proto_ipv4 = ""
        arp_dst_hw_mac = ""
        arp_dst_proto_ipv4 = ""
    if hasattr(raw_packet, "ipv6"):
        ipv6_src = raw_packet.ipv6.src
        ipv6_dst = raw_packet.ipv6.dst
    else:
        ipv6_src = ""
        ipv6_dst = ""
    return [
        time_epoch,
        frame_len,
        eth_src,
        eth_dst,
        ip_src,
        ip_dst,
        tcp_srcport,
        tcp_dstport,
        udp_srcport,
        udp_dstport,
        icmp_type,
        icmp_code,
        arp_opcode,
        arp_src_hw_mac,
        arp_src_proto_ipv4,
        arp_dst_hw_mac,
        arp_dst_proto_ipv4,
        ipv6_src,
        ipv6_dst,
    ]
