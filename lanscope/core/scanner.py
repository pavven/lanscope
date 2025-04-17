from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup


def network_scan(subnet='192.168.1.0/24'):
    print("Skanowanie sieci lan...")
    mac_lookup = MacLookup()

    # Arp packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=subnet)
    packet = ether / arp

    response = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for send, recived in response:
        ip = recived.psrc
        mac = recived.hwsrc
        try:
            vendor = mac_lookup.lookup(mac)
        
        except:
            vendor = "Nieznany"
        devices.append((ip,mac,vendor))

    print("\n[+] Znalezione urządzenia:")
    for ip, mac, vendor in devices:
        print(f"IP: {ip:15}, MAC: {mac:17}, Producent {vendor}")
        return devices
    