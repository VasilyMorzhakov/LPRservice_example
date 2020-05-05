#import httplib #python 2.7 version
import http.client as httplib #python 3 version
import time
import os

gate=os.environ['LPR_GATE']
server=os.environ['LPR_SERVER']
port=int(os.environ['LPR_PORT'])

conn = httplib.HTTPConnection(server, port) #open connection
f = open("example.jpg", "rb") # load image
data = f.read() #prepare image for transfer
f.close()
headers = {
        "Content-Type": "application/octet-stream",
        "Content-length": str(len(data)),
        "Accept": "text/plain",
        "GateCode": gate
    }
start = time.time()
conn.request("POST", "/test/", data, headers) #request recognition
rsp = conn.getresponse() #server response
data_received = rsp.read().decode() #result


print('response time ',time.time()-start)

print(data_received)
conn.close() 
