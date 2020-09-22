#########################################
# .: get_hosts.py :.
# Scans a /24 network or smaller to grab host information including IP, Mac and NIC Vendor
# Returns as text table or json with optional --json flag
# .: Usage (linux) - sudo required :.
# sudo ./get_hosts.sh $HOME 3.7.7 192.168.101.0/24
# where: 3.7.7 is your pyenv version and 192.168.101.0/24 is the network to scan
# Note: get_hosts.sh assumes you are using pyenv to manage your python versions.
#       alter get_hosts.sh as required for other installations
# .: Usage (windows) - sudo not required :.
# python get_hosts.py 192.168.101.0/24
# .: Dependencies :.
# python -m pip install python-nmap
# .: Other :.
# Author: Timothy C. Quinn
# Home: https://github.com/JavaScriptDude/get_hosts.py
# Licence: https://opensource.org/licenses/MIT
#########################################

import sys, nmap, json, ipaddress,argparse

argp = argparse.ArgumentParser(prog="get_hosts")

def printUsage(s: str):
    argp.print_help(s)
    # print("Usage: python get_hosts.py <network>")
    # if not s is None: print(s)
    sys.exit(0)

def main():

    argp.add_argument("-j", "--json", action='store_true')
    argp.add_argument("network", type=str)
    args = argp.parse_args()

    # Validate args
    if not args.network.strip() == '':
        try:
            ipa = ipaddress.ip_network(args.network, strict=True)
        except:
            printUsage("Invalid address passed: " + args.network)

        if not ipa.version == 4: 
            printUsage("Only IPV4 is supported at this time")
        elif ipa.num_addresses > 256: 
            printUsage("Please only specify a /24 network or smaller")  
    else:
        printUsage("Please pass a network")
    
    # execute nmap scan
    nm = nmap.PortScanner()
    nm.scan(hosts=args.network, arguments='-sP')

    lHosts=[]
    mRet = {'network': args.network, 'hosts': lHosts}

    # Scrape data
    for ip in nm.all_hosts():
        host = nm[ip]
        mac = "-"
        vendorName = "-"
        if 'mac' in host['addresses']:
            mac = host['addresses']['mac']
            if mac in host['vendor']:
                vendorName = host['vendor'][mac]

        status = host['status']['state']
        rHost = {'ip': ip, 'mac': mac, 'vendor': vendorName, 'status': status}
        
        lHosts.append(rHost)

    if args.json:
        # dump output as JSON
        print(json.dumps(mRet))
    else:
        import texttable as tt
        header1 = ['ip', 'mac', 'vendor', 'status']
        tbl = tt.Texttable(max_width=120)
        tbl.set_cols_align(list('r'*len(header1)))
        tbl.set_cols_dtype(list('t'*len(header1)))
        tbl.set_deco(tbl.HEADER | tbl.VLINES)
        tbl.header(header1)
        for rHost in mRet['hosts']:
            tbl.add_row([rHost['ip'], rHost['mac'], rHost['vendor'], rHost['status']])
        print(tbl.draw())


if __name__ == '__main__':
    main()
