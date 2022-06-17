#!usr/bin/env python

import netfilterqueue

# subprocess.call(["sudo", "iptables", "-I", "FORWARD -j NFQUEUE --queue-num 0"])
def process_packet(packet):
    print(packet)
    packet.accept()
    # packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

