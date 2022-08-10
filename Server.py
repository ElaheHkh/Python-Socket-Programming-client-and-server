# This Code is For Server
# Lets import Libraries
import socket, cv2, pickle, struct

# Socket Create
Server_socket= socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host_name= socket.gethostname()
print(host_name)
# make sure do it
host_ip = socket.gethostbyname(host_name)
print('Host_IP:',host_ip)
port =9999
socket_address = (host_ip,port)

# Socket Bind
Server_socket.bind (socket_address)

# socket Listen
Server_socket.listen (5)
print(" LISTENING AT: " , socket_address)

# Socket Accept
while True:
    client_socket, addr = Server_socket.accept ()
    print ('GOT CONNECTION FROM:' , addr)
    if client_socket:
        vid= cv2.VideoCapture(0)
        while (vid.isOepened()):
            img, frame = vid.read()
            a= pickle.dumps(frame)
            client_socket.sendall (message)
            cv2.imshow('TRANSMITTING VIDEO', frame)
            key= cv2.waitKey(1) & 0xFF
            if key == ord ('q'):
                client_socket.close()
                
            
