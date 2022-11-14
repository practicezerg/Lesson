def get_mac_from_ip(ip_address):
    try:
        output = subprocess.check_output(['arp', '-a', ip_address], encoding='utf-8')
        mac = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', output).group()
        mac = mac.replace('-', )
        mac = mac.replace(':', )
    except:
        mac = 'NO_MAC_FOUND'
    return mac

ip_adress = 192.168.0.1
a = get_mac_from_ip()
print(a)