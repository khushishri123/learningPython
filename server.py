# to implement socket programming then you have to import socket module
import socket
if __name__=="__main__":
    s=socket.socket()
    # we will be listening on port 9999
    s.bind(('localhost',9995))
    # here we will specify how many  requests it can listen in parallel
    s.listen(3)

    while True:
        print("Entered into the loop: ")
        c, addr=s.accept()
        print("Connected with: ",addr ,c)

        c.send(b"something")
        c.close()

