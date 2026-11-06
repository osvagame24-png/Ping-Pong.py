# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
font = pygame.font.Font(None, 500)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
ball_speedy = 200
ball_speedx = -200
ball_is_colaiding = False
score = 0

player_pos = pygame.Vector2(20, screen.get_height() / 2)
ball_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() / 2)
npc_pos = pygame.Vector2(screen.get_width() /1.01 , screen.get_height() / 2)
wall_pos = pygame.Vector2(screen.get_width() /2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    pygame.draw.rect(screen, "gray", (wall_pos.x - 0, wall_pos.y - 1000, 40, 2000))
    score_surface = font.render(str(score), True, "gray")
    screen.blit(score_surface, (200,200))
    pygame.draw.rect(screen, "black", (ball_pos.x - 20, ball_pos.y - 20, 40, 40))
    pygame.draw.rect(screen, "#8b0000", (npc_pos.x - 20, npc_pos.y - 20, 40, 200))
    pygame.draw.rect(screen, "black", (player_pos.x - 20, player_pos.y - 20, 40, 200))


    ball_rect = pygame.Rect(ball_pos.x, ball_pos.y, 40, 40)
    npc_rect = pygame.Rect(npc_pos.x, npc_pos.y - 20, 40, 200)
    player_rect = pygame.Rect(player_pos.x, player_pos.y - 20, 40, 200)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt


    if player_pos.y > screen.get_height() / 1.31:
        player_pos.y -= 10
    elif player_pos.y < screen.get_height() / 40:
        player_pos.y += 10


    ball_pos.x += ball_speedx * dt
    ball_pos.y += ball_speedy * dt


    if ball_is_colaiding == False:
        if ball_rect.colliderect(player_rect):
            ball_speedx *= -1
            score += 1
            ball_is_colaiding = True
        elif ball_rect.colliderect(npc_rect):
            ball_speedx *= -1
            ball_is_colaiding = True
        elif ball_pos.x > screen.get_width() / 1.025:
            break
        elif ball_pos.x < screen.get_width() / 40:
            break

    if ball_is_colaiding == True:
        if not ball_rect.colliderect(player_rect) and not ball_rect.colliderect(npc_rect):
            ball_is_colaiding = False
        

    if ball_pos.y > screen.get_height() / 1.025:
        ball_speedy *= -1
    elif ball_pos.y < screen.get_height() / 40:
        ball_speedy *= -1

    npc_pos.y += (ball_pos.y - npc_pos.y) * 0.1

    if npc_pos.y > screen.get_height() / 1.30:
        npc_pos.y -= 20
    elif npc_pos.y < screen.get_height() / 40:
        npc_pos.y += 10



    pygame.display.flip()

    dt = clock.tick(60) / 1000


