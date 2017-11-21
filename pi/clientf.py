import socket
import pygame

host=socket.gethostname()
port=5555

screen = pygame.display.set_mode((640,480))

while 1:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)
    conn, addr = s.accept()
    message = []
    while True:
        d = conn.recv(1024*1024)
        if not d: break
        else: message.append(d)
    data = ''.join(message)
    image = pygame.image.fromstring(data,(640,480),"RGB")
    screen.blit(image,(0,0))
    pygame.display.update()