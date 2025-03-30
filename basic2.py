import pygame as pp
pp.init()

screen = pp.display.set_mode((800,600))
run = True

x=200
y=200
width=50
height=70
vel=2
g = 3

obs = pp.Rect(200,200,120,30)

while run:
    player= pp.Rect(x,y,width,height)
    for event in pp.event.get():
        if event.type==pp.QUIT:
            run= False

    keys = pp.key.get_pressed()
    if keys[pp.K_SPACE]and y > vel:
        y-=5.5
    if y< 600 -height:
        y+=g
    if keys[pp.K_d]and x < 800:
        x+=vel
    if keys[pp.K_a]and x > vel:
        x-=vel
    #detectes if player hits the other rectangle 
    if player.colliderect(obs):
        print("hit")
        y=obs.top-height

    screen.fill((0,0,0))
    pp.draw.rect(screen,(0,69,69),player)
    pp.draw.rect(screen,(0,69,69),obs)
    pp.display.update()
    
    