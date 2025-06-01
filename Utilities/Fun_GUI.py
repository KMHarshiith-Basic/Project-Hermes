import os, sys, random, time

# Temporarily suppress stdout
original_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
import pygame
# Restore stdout
sys.stdout.close()
sys.stdout = original_stdout

def Boss(A):
    pygame.init()
    time.sleep(3)

    # Set up display
    WIDTH, HEIGHT = 800, 600
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("AI_Bot: Final Override")

    # Loading Images
    player_img = pygame.image.load("Utilities/player.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (75, 33)).convert_alpha()

    boss_img = pygame.image.load("Utilities/boss.png").convert_alpha()
    boss_img = pygame.transform.scale(boss_img, (206, 53)).convert_alpha()
    boss_img.set_colorkey((255, 255, 255))  # RGB for white

    a = (2500-A)//100  # Adjust the frequency of enemy bullets based on the difficulty level
    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 50, 50)
    BLUE = (50, 150, 255)
    BLACK = (0, 0, 0)

    # Clock
    clock = pygame.time.Clock()

    # Player settings
    player = pygame.Rect(370, 500, 75, 33)
    player_speed = 7

    # Boss settings
    boss = pygame.Rect(300, 50, 206, 53)
    boss_health = 30

    # Bullets (logic blasts)
    bullets = []
    enemy_bullets = []

    # Game loop
    running = True
    player_health = 5

    while running:
        clock.tick(60)
        win.fill(BLACK)

        # Draw entities
        win.blit(player_img, (player.x, player.y))
        win.blit(boss_img, (boss.x, boss.y))

        # Health bar
        pygame.draw.rect(win, RED, (10, 10, boss_health * 5, 10))
        pygame.draw.rect(win, BLUE, (10, 30, player_health * 25, 10))

        # Handle bullets
        for bullet in bullets[:]:
            bullet.y -= 10
            pygame.draw.rect(win, WHITE, bullet)
            if bullet.colliderect(boss):
                boss_health -= 1
                bullets.remove(bullet)
            elif bullet.y < 0:
                bullets.remove(bullet)

        # Boss attacks
        if random.randint(1, a) == 1:
            enemy_bullets.append(pygame.Rect(random.randint(boss.x, boss.x + boss.width), boss.y + 40, 10, 10))

        for e_bullet in enemy_bullets[:]:
            e_bullet.y += 7
            pygame.draw.rect(win, RED, e_bullet)
            if e_bullet.colliderect(player):
                player_health -= 1
                enemy_bullets.remove(e_bullet)
            elif e_bullet.y > HEIGHT:
                enemy_bullets.remove(e_bullet)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Keypress
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:  # limit bullet spam
                bullets.append(pygame.Rect(player.x + 25, player.y, 10, 10))

        # End conditions
        if boss_health <= 0:
            print("YOU WIN! The Cyber Assassin was taken down.")
            running = False
            pygame.quit()
            return 0
        if player_health <= 0:
            print("YOU LOSE! The Assassin Escaped.")
            running = False
            pygame.quit()
            return 1

        pygame.display.update()

#Boss(500)  # Example difficulty level, can be adjusted