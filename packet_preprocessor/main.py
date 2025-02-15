import pyshark
from packet_parser import parse_packet
from packet_processor import process_packets
from collections import deque
from predictor import predict
from packet_capture import capture_packets_with_interval
import os
import tempfile

last_processed_time = 0

def capture_packets(interface: str, duration: int) -> deque:
    """ Captures packets for the given duration and stores them in a deque. """
    print(f"Capturing packets on {interface} for {duration} seconds...")

    with tempfile.NamedTemporaryFile(suffix=".pcap", delete=False) as temp_pcap:
        temp_filename = temp_pcap.name

    os.system(f"tshark -i {interface} -a duration:{duration} -w {temp_filename}")  # Run Wireshark CLI

    packets = pyshark.FileCapture(temp_filename)
    
    packet_deque = deque()
    
    for packet in packets:
        packet_deque.append(packet)  # Store packets in deque

    packets.close()
    os.remove(temp_filename)  # Clean up temp file

    print(f"Captured {len(packet_deque)} packets.")
    return packet_deque

# ✅ Capture packets and store in a deque
packets_deque = capture_packets("en0", 10)

vectors = process_packets(packets_deque)
print(vectors.shape)

# ✅ Pass deque to preprocessor
# Example: process_packets(packets_deque)
# for packet in packets_deque:
#     print(packet)  # Modify this to send packets to your preprocessor
#


# # capture = pyshark.LiveCapture(interface='docker0')
# capture = capture_packets_with_interval(10)
# print("done with you")
# packets = deque([])
# for raw_packet in capture:
#     print(raw_packet)
#     # packets.append(parse_packet(raw_packet))
#     # while (float(raw_packet.frame_info.time_epoch) - float(packets[0][0]) > 10):
#     #     packets.popleft()
#     # if (float(raw_packet.frame_info.time_epoch) - last_processed_time > 5):
# # vectors = process_packets(packets)
# # print(vectors.shape)
# # predict(vectors)
# # last_processed_time = float(raw_packet.frame_info.time_epoch)
