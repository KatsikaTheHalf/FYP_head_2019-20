import socket
import face
import keyboard
import time
# Connect to target IP
TCP_IP = 'raspberrypi.local'
TCP_PORT_x = 9982
TCP_PORT_y = TCP_PORT_x + 1
BUFFER_SIZE = 4096

# Establish connection
print('Establishing connection...\n(', TCP_IP, ':', TCP_PORT_x,')')
xSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
xSocket.connect((TCP_IP, TCP_PORT_x))
print('Connection established!')
print('Establishing connection...\n(', TCP_IP, ':', TCP_PORT_y,')')
ySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ySocket.connect((TCP_IP, TCP_PORT_y))
print('Connection established!')

# Initiate face recognition
faces = face.FACE()

while(faces.getCap()):
    faces.observe()
    xCenter = faces.getxCenter()
    yCenter = faces.getyCenter()
    # senddata = 1000*xCenter+yCenter
    xSocket.send(str(xCenter).encode('utf-8'))
    ySocket.send(str(yCenter).encode('utf-8'))
    # echo = s.recv(BUFFER_SIZE)
    # print('Server echo: ', echo)
    if keyboard.is_pressed('q'):
        xSocket.send(str(-1).encode('utf-8'))
        break
    time.sleep(0.1)

xSocket.close()
ySocket.close()