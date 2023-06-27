from scapy.all import *
import os
import configuration_parser
import filterCommunication
import iptc

interfaceMapping = {
    "eth0": "eth1",
    "eth1": "eth0"
}


def startup():
    # disable unused interfaces
    for interface in get_if_list():
        if not interface in interfaceMapping.keys():
            os.system("ifconfig " + interface + " down")

    # enable interfaces
    for interface in interfaceMapping.keys(): 
        os.system("ip link set " + interface + " promisc on")


def main():
    ipTable = configuration_parser.parse("file-path")
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "FORWARD")
    
    for key in ipTable:
        rule =  iptc.Rule()
        rule.protocol = "tcp"
        rule.src = key[0]
        rule.sport = key[1]
        rule.dst = ipTable[key][0]
        rule.dport = ipTable[key][1]
        rule.target = iptc.Target(rule, "ACCEPT")
        chain.insert_rule(rule)
        

if __name__ == '__main__':
    startup()
    main()
