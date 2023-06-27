from scapy.all import *
import os
import configuration_parser
import filterCommunication

FILE_PATH = "conf.json"

interfaceMapping = {
    "ens3": "ens5",
    "ens5": "ens3",
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
        
    #os.system("sudo iptables -t filter --append FORWARD -j DROP")

    command = ""
    start = "sudo iptables -t filter --append FORWARD"
    end = " -j ACCEPT"
        
    for key in ipTable:
        command = ""
        command += start
        command += " -s " + key[0]
        command += " -d " + ipTable[key][0]
        command += " -p tcp"
        command += " --sport " + key[1]
        command += " --dport " + ipTable[key][1]
        command += end
        os.system(command)
    os.system("sudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT")
    os.system("sudo iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT")


if __name__ == '__main__':
    startup()
    main()
