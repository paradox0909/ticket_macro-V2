import time
from scapy.all import IP, ICMP, send

def send_packet(destination_ip, packet_number):
    packet = IP(dst=destination_ip) / ICMP()
    send(packet, verbose=False)
    print(f"ping good - Packet {packet_number}")

if __name__ == "__main__":
    target_ip = ""
    # set ip first
    packet_count = 3 
    interval = 0.001    
    

    for i in range(1, packet_count + 1):
        send_packet(target_ip, i)
        time.sleep(interval)

    for i in range(packet_count):
        send_packet(target_ip, i + packet_count + 1)
        time.sleep(interval)
