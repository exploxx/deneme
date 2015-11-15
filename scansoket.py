import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server= '192.168.1.1'

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False
print('------------------')        
for x in range(1,67):
    if pscan(x):
        print('Port',x,'is open')
    else:
        print('Port',x,'is closed')
        