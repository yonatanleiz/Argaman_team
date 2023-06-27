from scapy.all import *
import os
import configuration_parser
import filterCommunication

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
    
    while True:
        try:
            capture = sniff(count=1)[0]
        except OSError as E:
            print("No open interfaces")
            
            
def inspect_packet():
    try:
        if (filterCommunication.checkSrcAndDst(ipTable, capture):
            srp(capture, iface=interfaceMapping[capture.sniffed_on])
    except KeyError as E:
        print("routing failed")
    return


if __name__ == '__main__':
    startup()
    main()
