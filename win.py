import pygame
pygame.init()


display_surface = pygame.display.set_mode((500, 500))

font = pygame.font.Font(None, 32)
text = font.render('u win', True, (255,255,255))

while True:
	display_surface.fill((0,0,0))
	display_surface.blit(text,(200,200))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		
		pygame.display.update()



