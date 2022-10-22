import dns.zone
import dns.resolver

address = str(input("What needs transfering?: "))

resolver = dns.resolver.Resolver()
ns_servers=[]

def dns_zone_transfer(address):
    ns_answer = resolver.resolve(address, 'NS')
    for server in ns_answer:
        print("Found NS {}".format(server))
    ip_answer = resolver.resolve(server.target, 'A')
    for ip in ip_answer:
        print("IP for {} is {}".format(server, ip))
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(str(ip), address))
        for host in zone:
            print("Found Host: {}".format(host))
    except Exception as e:
        print("NS {} Refused Zone Transfer".format(server))
        pass
    
dns_zone_transfer(address)