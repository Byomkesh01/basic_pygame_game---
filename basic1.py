import pygame as pp

pp.init()


screen = pp.display.set_mode((800, 600))
pp.display.set_caption("ayyy")


x, y = 100, 300
width=50 
height = 50
vel = 2.9


run = True
while run:
   

    for event in pp.event.get():
        if event.type == pp.QUIT:
            run = False

    keys = pp.key.get_pressed()

    # Left and right movement
    if keys[pp.K_a] and x > vel:
        x -= vel
    if keys[pp.K_d] and x < 800 - width:
        x += vel

    # Jumping (Original Code)
    if keys[pp.K_w] and y > vel:
        y -= vel

    # Apply gravity
    if keys[pp.K_s] and y < 600 - height:
        y += vel

    # Collision detection (stand on platform)
    player = pp.Rect(x, y, width, height)
    

    # Draw everything
    screen.fill((0, 0, 0))
   
    pp.draw.rect(screen, (0, 255, 0), player)  # Player
    pp.display.update()

pp.quit()
