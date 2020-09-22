#########################################
# .: get_hosts.py :.
# Scans a /24 network or smaller to grab host information including IP, Mac and NIC Vendor
# Returns as data JSON
# .: Usage (linux) - sudo required :.
# sudo ./get_hosts.sh $HOME 3.7.7 192.168.101.0/24
# Note: get_hosts.sh assumes you are using pyenv to manage your python versions.
#       alter get_hosts.sh as required for other installations
# where: 3.7.7 is your pyenv version and 192.168.101.0/24 is the network to scan
# .: Usage (windows) - sudo not required :.
# python get_hosts.py 192.168.101.0/24
# .: Dependencies :.
# python -m pip install python-nmap
# .: Other :.
# Author: Timothy C. Quinn
# Home: https://github.com/JavaScriptDude/get_hosts.py
# Licence: https://opensource.org/licenses/MIT
#########################################

import sys, nmap, json, ipaddress

def printUsage(s):
    print("Usage: python get_hosts.py <network>")
    if not s is None: print(s)
    sys.exit(0)

def main(argv):
    nm = nmap.PortScanner()
    # Validate args
    if len(argv) == 1 and not argv[0].strip() == '':
        address=argv[0]
        try:
            ipa = ipaddress.ip_network(address, strict=True)
        except:
            printUsage("Invalid address passed: " + address)

        if not ipa.version == 4: 
            printUsage("Only IPV4 is supported at this time")
        elif ipa.num_addresses > 256: 
            printUsage("Please only specify a /24 network or smaller")  
    else:
        printUsage()
    
    # execute nmap scan
    nm.scan(hosts=address, arguments='-sP')

    lHosts=[]
    mRet = {'network': address, 'hosts': lHosts}

    # Scrape data
    for ip in nm.all_hosts():
        host = nm[ip]
        print(host)
        mac = "-"
        vendorName = "-"
        if 'mac' in host['addresses']:
            mac = host['addresses']['mac']
            if mac in host['vendor']:
                vendorName = host['vendor'][mac]

        status = host['status']['state']
        rHost = {'ip': ip, 'mac': mac, 'vendor': vendorName, 'status': status}
        
        lHosts.append(rHost)

    # dump output as JSON
    print(json.dumps(mRet))


if __name__ == '__main__':
    main(sys.argv[1:])
