import socket

greeting = """                   URL Trace\n
                by Ty Valentine """
                
print(greeting)

url = str(input("What is the URL that you would like to trace? >> "))

ipaddr = socket.gethostbyname(url)

print(f"The IP of {url} is " + ipaddr)
