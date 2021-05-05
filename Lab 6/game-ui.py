from pygame.locals import *
import pygame
import time
import paho.mqtt.client as mqtt
import uuid
import signal



class Player:
    x = 44
    y = 44
    speed = 1
 
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed
 
class Maze:
    def __init__(self):
        self.M = 10
        self.N = 8
        self.maze = [ 1,1,1,1,1,1,1,1,1,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,0,1,1,1,1,1,1,0,1,
                    1,0,1,0,0,0,0,0,0,1,
                    1,0,1,0,1,1,1,1,0,1,
                    1,0,0,0,0,0,0,0,0,1,
                    1,1,1,1,1,1,1,1,1,1,]

    def draw(self,display_surf,image_surf):
        pass
        bx = 0
        by = 0
        for i in range(0,self.M*self.N):
            if self.maze[ bx + (by*self.M) ] == 1:
                display_surf.blit(image_surf,( bx * 44 , by * 44))
        
            bx = bx + 1
            if bx > self.M-1:
                bx = 0 
                by = by + 1


topic = 'IDD/juicey/labyrinth'

x_msg = 0.0
y_msg = 0.0

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
        self.maze = Maze()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("ball.png").convert()
        self._block_surf = pygame.image.load("wall.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
    
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf, self._block_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            global x_msg
            global y_msg
            if (keys[K_RIGHT] or x_msg > 1):
                self.player.moveRight()
 
            if (keys[K_LEFT] or x_msg < -1):
                self.player.moveLeft()
 
            if (keys[K_UP] or y_msg > 1):
                self.player.moveUp()
 
            if (keys[K_DOWN] or y_msg < -1):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)

def on_message(cleint, userdata, msg):
    # if a message is recieved on topic, print message
    if msg.topic == topic:
        x, y = list(map(int, msg.payload.decode('UTF-8').split(',')))
        x_msg = x
        y_msg = y

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
    theApp = App()
    
    theApp.on_execute()