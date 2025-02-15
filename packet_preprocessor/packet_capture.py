import os
import pyshark
import time

def capture_packets_with_interval(duration: int) -> list:
    packets = []
    '''Captures packets in the specified interval, 
    adds it to a list and returns it everytime the interval ends'''
    os_name = os.name
    if os_name == "nt":
        interface = "Wi-Fi" 
    elif os_name == "posix":
        interface = "en0"  
    else:
        print("Unidentified OS!")
        exit(0)

    # try:
    #     duration = int(input("Enter packet capture duration (in seconds): "))
    # except ValueError:
    #     print("Invalid input! Please enter a valid number.")
    #     exit(1)

    print(f"Capturing packets on {interface} for {duration} seconds...\n")

    capture = pyshark.LiveCapture(interface=interface)
    start_time = time.time()

    for packet in capture.sniff_continuously():
        if time.time() - start_time > duration:
            break

        # try:
        #     protocol = packet.transport_layer          
        #     src_ip = packet.ip.src
        #     dst_ip = packet.ip.dst
        #     src_port = packet[protocol].srcport
        #     dst_port = packet[protocol].dstport

        packets.append(f"{packet}")

    capture.close()
    return packets

if __name__ == "__main__":
    timer = int(input("Enter time interval: "))
    packets = capture_packets_with_interval(timer)
    output = f"📡 Captured Packets ({timer} sec):\n" + "\n".join(packets)
    print(output)
