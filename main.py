import pygame as pp
import random
#import win
pp.init()

def show_win_screen(screen):
    font = pp.font.Font(None, 74)  # Create font (default, size 74)
    win_text = font.render("You Win!", True, (255, 255, 255))  # White text

    screen.fill((0, 0, 0))  # Black background
    screen.blit(win_text, (300, 250))  # Draw text at (x, y)
    pp.display.update()  # Refresh screen
    pp.time.delay(2000)  # Show for 2 seconds


screen = pp.display.set_mode((800,600))
pp.display.set_caption("newnew")

run = True

#character position and size and speed
x=0
y=0
width=50
height=50
vel=2.5
gravity =2

nx = random.randint(2,750)
ny = random.randint(0,260)

win= pp.Rect(nx,ny,width,height)



#obstical
obstical = []
#random position and size of obsticals
for i in range(5):
    obsx=random.randint(100,700)
    obsy=random.randint(100,600)
    obs_width=random.randint(20,30)
    obs_height=random.randint(100,200)
    obstical.append(pp.Rect(obsx,obsy,obs_height,obs_width))


while run:
    screen.fill((0,0,0))
    player = pp.Rect(x, y, width, height)
  #quit game
    for event in pp.event.get():
        if event.type == pp.QUIT:
            run = False


    #chekcing for key press
    keys = pp.key.get_pressed()
    if keys[pp.K_SPACE] and y>vel:
        y-=5.5   
    if y<600-height:
        y+=gravity
    if keys[pp.K_a] and x> vel:
        x-=vel
    if keys[pp.K_d] and x<800-width:
        x+=vel

    #detech collision for all objects
    for obs in obstical:
        if player.colliderect(obs):
            y=obs.top-height
    #draw all the obsticals 
    for obs in obstical:
        pp.draw.rect(screen,(255,255,255),obs)
    
   

    if player.colliderect(win):
        show_win_screen(screen)
        run = False

    #surface,color,position,size ,
    pp.draw.rect(screen,(255,20,20),win)
    pp.draw.rect(screen,(0,69,69),player)# player
    
    
    print(x,y)
    pp.display.update()

