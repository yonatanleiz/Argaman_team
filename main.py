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

    command = ""
    start = "sudo iptables -t filter --check FORWARD"
    end = "-j ACCEPT"
        
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "FORWARD")
    chain.flush()
    rule =  iptc.Rule()
    rule.target = iptc.Target(rule, "DROP")
    chain.insert_rule(rule)
        
    for key in ipTable:
        command = ""
        command += start
        commend += " -p tcp"
        command += " -s " + key[0]
        command += " -d " + ipTable[key][0]
        command += " -sport " + key[0]
        command += " -dport " + ipTable[key][0]
        command += end
        os.system(command)
        

if __name__ == '__main__':
    startup()
    main()
