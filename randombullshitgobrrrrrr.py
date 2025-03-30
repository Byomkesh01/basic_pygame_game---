import pygame as pp
import random
pp.init()

screen = pp.display.set_mode((800, 600))
pp.display.set_caption("newnew")

run = True

# Character properties
x, y = 0, 0
width, height = 50, 50
vel = 2.9
gravity = 2

# Obstacles list
object = []

for i in range(6):  # Generate 5 random obstacles
    obsx = random.randint(100, 800)  # Random x position
    obsy = random.randint(100, 600)  # Random y position
    obs_width = random.randint(20, 30)  # Random width
    obs_height = random.randint(100, 200)  # Random height
    object.append(pp.Rect(obsx, obsy, obs_height, obs_width))  # Fixed 'Rect()' issue

while run:
    player = pp.Rect(x, y, width, height)  # Define player rectangle

    # Quit game
    for event in pp.event.get():
        if event.type == pp.QUIT:
            run = False

    # Checking for key press
    keys = pp.key.get_pressed()
    if keys[pp.K_SPACE] and y > vel:
        y -= 5.5  # Jump
    if y < 600 - height:
        y += gravity  # Apply gravity
    if keys[pp.K_a] and x > vel:
        x -= vel  # Move left
    if keys[pp.K_d] and x < 800 - width:
        x += vel  # Move right

    # Collision detection (stand on platform)
    for obs in object:
        if player.colliderect(obs) and gravity > 0:
            y = obs.top - height  # Place player on top of obstacle

    # Drawing
    screen.fill((0, 0, 0))  # Clear screen
    pp.draw.rect(screen, (0, 69, 69), player)  # Draw player

    for obs in object:
        pp.draw.rect(screen, (255, 0, 0), obs)  # Draw obstacles

    print(x, y)  # Debugging position
    pp.display.update()  # Update screen

pp.quit()

