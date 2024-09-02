import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = [0,0]
pygame.display.set_caption("Ball Is Life - Asad")
fontWindow = pygame.font.SysFont("Arial", 24)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
titleText = fontWindow.render("Ball - Asad Alli 2024",True, "white")

while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(titleText,(0,0))

    pygame.draw.circle(screen, "white", player_pos, 20)

    pygame.draw.circle(screen, "red", [50, 100], 24)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 50 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 50 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 50 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 50 * dt

    #out of bounds check
    if player_pos.x > screen.get_width():
        player_pos.x = player_pos.x - screen.get_width()
    elif player_pos.x < 0.2:
            player_pos.x = player_pos.x + screen.get_width()

    if player_pos.y > screen.get_height():
            player_pos.y = player_pos.y - screen.get_height()
    elif player_pos.y < 0.2:
            player_pos.y = player_pos.y + screen.get_height()

    pygame.display.flip()
    dt = clock.tick(60) / 100
pygame.quit()