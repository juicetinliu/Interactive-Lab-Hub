from pygame.locals import *
import pygame
import time
import paho.mqtt.client as mqtt
import uuid
import signal
import random
import math


class Player:
    x = 400
    y = 300
    speed = 1
 
    def moveRight(self, amt = None):
        if amt is None:
            self.x = self.x + self.speed
        else:
            self.x = self.x + amt
 
    def moveLeft(self, amt = None):
        if amt is None:
            self.x = self.x - self.speed
        else:
            self.x = self.x - amt
 
    def moveUp(self, amt = None):
        if amt is None:
            self.y = self.y - self.speed
        else:
            self.y = self.y - amt
 
    def moveDown(self, amt = None):
        if amt is None:
            self.y = self.y + self.speed
        else:
            self.y = self.y + amt
 
class Hole:
    def __init__(self):
        self.x = random.randrange(100, 700)
        self.y = random.randrange(100, 500)

    def regenHole(self):
        self.x = random.randrange(100, 700)
        self.y = random.randrange(100, 500)

topic = 'IDD/juicey/labyrinth/#'

topicq = 'IDD/juicey/labyrinth'
# topicX = 'IDD/juicey/labyrinth/X'
# topicY = 'IDD/juicey/labyrinth/Y'

# x_msg = 0.0
# y_msg = 0.0

class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.hole = Hole()
        self.controls = [0.0, 0.0]
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("ball.png").convert()
        self._block_surf = pygame.image.load("hole.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        if math.dist([self.player.x, self.player.y], [self.hole.x, self.hole.y]) < 40:
            self.hole.regenHole()
    
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self._display_surf.blit(self._block_surf,(self.hole.x,self.hole.y))
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            moves = list(map(abs, self.controls))
            if self.controls[0] > 0.5:
                self.player.moveRight(moves[0] - 0.5)
 
            if self.controls[0] < -0.5:
                self.player.moveLeft(moves[0] - 0.5)
 
            if self.controls[1] > 0.5:
                self.player.moveUp(moves[1] - 0.5)
 
            if self.controls[1] < -0.5:
                self.player.moveDown(moves[1] - 0.5)
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()

theApp = App()

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)

def on_message(cleint, userdata, msg):
    # if a message is recieved on topic, print message
    if topicq in msg.topic:
        player_axis = 0 if msg.topic[-1] == 'X' else 1
        m = float(msg.payload.decode('UTF-8'))
        theApp.controls[player_axis] = m
    
    if topic in msg.topic:
        m = msg.payload.decode('UTF-8').split(',')
        theApp.controls[player_axis] = list(map(float, m))

# this lets us exit gracefully (close the connection to the broker)
def handler(signum, frame):
    print('exit gracefully')
    client.loop_stop()
    exit (0)

# hen sigint happens, do the handler callback function
signal.signal(signal.SIGINT, handler)


if __name__ == "__main__" :
    client = mqtt.Client(str(uuid.uuid1()))
    client.tls_set()
    client.username_pw_set('idd', 'device@theFarm')
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(
        'farlab.infosci.cornell.edu',
        port=8883)

    client.loop_start()
    
    theApp.on_execute()