from scapy.all import *


def checkSrcAndDst(ipTable, packet):
    """
    Checks source (ip and port) and destination couple against allowed ip table.
    Returns True if passed check, False otherwise.
    """
    srcIp = packet
    srcPort = packet
    destIp = packet
    destPort = packet
    
    srcSet = [srcIp, srcPort]
    destSet = [destIp, destPort]
    
    if (srcSet in ipTable):
        if (destSet == ipTable[srcSet]):
            return True
    return False

