import socket
import pygame
import time

host = socket.gethostname()
port = 5555
pygame.init()
image = pygame.surface.Surface((640, 480))
i=0
j=0
while 1:
    image.fill((i,j,0))
    i+=10
    j+=5
    if i >= 255: i = 0
    if j >= 255: j = 0
    data = pygame.image.tostring(image,"RGB")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(data)
    s.close()
    time.sleep(0.5)
