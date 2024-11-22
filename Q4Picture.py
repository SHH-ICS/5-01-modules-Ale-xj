import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Picture")

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

screen.fill(WHITE)
pygame.draw.rect(screen, RED, (50, 50, 200, 100))
pygame.draw.circle(screen, BLUE, (400, 200), 70)
pygame.draw.ellipse(screen, GREEN, (150, 200, 300, 150))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
