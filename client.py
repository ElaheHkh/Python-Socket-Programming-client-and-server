
# lets make the client code
import socket, cv2, pickle, struct

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip= '192.168.1.20'
port= '9999'
print("%s is listening on TCP port %s" % (host_ip,port))

client_socket.connect((host_ip,int(port))) # a tuple
data=b""
payload_size= struct.calsize("Q")
while True:
    while len (data) < payload_size:
        packet = client_socket.recv(4*1024) # 4K
        if not packet: break
        data += packet
    packed_msg_size= data [:payload_size]
    data= data[payload_size:]
    msg_size= struct.unpack ( "Q", packed_msg_size)[0]
    
    while len (data) < msg_size:
        data += client_socket.recv (4*1024)
    frame_data = data [:msg_size]
    data = data [ msg_size:]
    frame_data= pickle.loads(frame_data)
    cv2.imshow("Received", frame)
    key = cv2.waitKey (1) & 0xFF
    if key == ord (''):
        break
client_socket.close()
      
