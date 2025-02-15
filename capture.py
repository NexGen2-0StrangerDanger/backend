import os
import pyshark
import time

# Get OS info and set the network interface
os_name = os.name
if os_name == "nt":
    interface = "Wi-Fi"  # Adjust if needed
elif os_name == "posix":
    interface = "en0"  # Adjust based on your system (e.g., "eth0", "wlan0")
else:
    print("Unidentified OS!")
    exit(0)

# Get capture duration from user input
try:
    duration = int(input("Enter packet capture duration (in seconds): "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit(1)

print(f"Capturing packets on {interface} for {duration} seconds...\n")

# Capture packets
capture = pyshark.LiveCapture(interface=interface)
start_time = time.time()
packet_summary = []

for packet in capture.sniff_continuously():
    if time.time() - start_time > duration:
        break  # Stop capturing after user-defined time

    try:
        protocol = packet.transport_layer  # TCP, UDP, etc.
        src_ip = packet.ip.src
        dst_ip = packet.ip.dst
        src_port = packet[protocol].srcport
        dst_port = packet[protocol].dstport

        packet_summary.append(
            f"{protocol} Packet: {src_ip}:{src_port} → {dst_ip}:{dst_port}"
        )
    except AttributeError:
        continue  # Skip packets without IP/protocol info

capture.close()

# Combine and print output
output = f"📡 Captured Packets ({duration} sec):\n" + "\n".join(packet_summary)
print(output)
