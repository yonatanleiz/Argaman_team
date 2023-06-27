from scapy.all import *
import os
import configuration_parser
import filterCommunication
import iptc

FILE_PATH = "conf.json"

interfaceMapping = {
    "ens33": "ens38",
    "ens38": "ens33",
    "lo": "lo"
}


def startup():
    # disable unused interfaces
    for interface in get_if_list():
        if not interface in interfaceMapping.keys():
            os.system("ifconfig " + interface + " down")

    # enable interfaces
    for interface in interfaceMapping.keys(): 
        os.system("ifconfig " + interface + " up")
        os.system("ip link set " + interface + " promisc on")


def main():
    ipTable = configuration_parser.parse(FILE_PATH)
    if not ipTable:
        print("exiting...")
        exit()
        
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "FORWARD")
    chain.flush()
    rule =  iptc.Rule()
    rule.target = iptc.Target(rule, "DROP")
    chain.insert_rule(rule)
        
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
