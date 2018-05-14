# Main gui

#Include files here:
import pygame
import os

# Setup
FPS = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (173,255,47)
BLUE = (0, 0, 255)
PEACH_1 = (205,175,149)
PEACH_2 = (255,218,185)
YELLOW = (255,255,0)
ORANGE = (218,165,32)
GRAY = (190,190,190)
LIGHT_GRAY = (211,211,211)
LIGHT_BLUE = (135,206,250)
DARK_GREY = (105,105,105)

game_folder = os.path.dirname(__file__) #Find file location
# location = os.path.join(game_folder, 'filename') #Use this to grab files that are in the same directory

pygame.init()
infoObject = pygame.display.Info() #Screen info

WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Use the max screen
pygame.display.set_caption('Smart house') #Name
clock = pygame.time.Clock()


#BackGround = Background(os.path.join('bg_shroom.bmp'), [0,0]) #If a background wants to be used.

# Functions
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def message_display(s,text,x,y): #freesansbold.ttf
    largeText = pygame.font.Font('freesansbold.ttf',s)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def buttons(s,msg,x,y,w,h,ic,ac,number_1,action = None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if action != None and click[0] == 1:
            action(number_1)
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",s)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)




def main(running):
    # Process input (events)
    # Update
    # Render (draw)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
    
        
        
        #screen.blit(BackGround.image, BackGround.rect) #image
        screen.fill(LIGHT_GREEN) #Color
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        pygame.display.flip()




    print('Closing')
    pygame.quit()

if __name__ == "__main__":
    main(1)


