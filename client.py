import socket
if __name__=="__main__":
    s=socket.socket()
    # now we have to connect with the server by passing localhost and port number . Basically we have to pass an object that contains
    # IP and port number, port number that we are passing is 9999
    s.connect(('localhost',9995))
    # recv(1024) method will print bytes,so to convert it into string we will call decode()  method
    print(s.recv(1024).decode())

