import socket
import random
#socket.gethostbyname(socket.gethostname())
def GET(url):
    response = str()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            sock.bind(("192.168.1.3", random.randint(1001, 65535)))
            break
        except:
            pass
    url = url.split("/")
    url.remove(url[1])
    resource = str()
    if(len(url)<3):
        request = f"HEAD \ HTTP/1.1\r\nHost:{url[1]}\r\n\r\n"
    else:
        request = f"HEAD {resource} HTTP/1.1\r\nHost:{url[1]}\r\n\r\n"

    for i in url[2::]:
        resource = resource + "/"+i
    request = f"HEAD {resource} HTTP/1.1\r\nHost:{url[1]}\r\n\r\n"
    sock.connect((socket.gethostbyname(url[1]), 80))
    sock.send(request.encode("UTF-8"))
    response = sock.recv(1024).decode("UTF-8")
    response1 = response.split()
    response_len = 0
    sock.close()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            sock.bind(("192.168.1.3", random.randint(1001, 65535)))
            break
        except:
            pass
    sock.connect((socket.gethostbyname(url[1]), 80))
    request = f"GET {resource} HTTP/1.1\r\nHost:{url[1]}\r\n\r\n"
    response_len = int(response1[response1.index("Content-Length:")+1])
    sock.send(request.encode("UTF-8"))
    response2 = sock.recv(len(response)+response_len)
    print(response2)
    sock.close()
    return response2.decode("UTF-8")
print(GET("http://info.cern.ch/hypertext/WWW/TheProject.html"))