import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((832, 896))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

map_layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 3, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 3, 1, 0, 1],
    [1, 0, 1, 3, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 3, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 3, 1, 0, 1],
    [1, 0, 1, 3, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 3, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 2, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

original_pacman_frames = [pygame.image.load('ezgif-3-fca9bb9f8a.gif') for i in range(1, 5)]
blue_enemy_img = pygame.image.load('images__1_-removebg-preview (1).png')
orange_enemy_img = pygame.image.load('2469743-orange-removebg-preview (1).png')

font = pygame.font.Font(None, 36)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_frames = original_pacman_frames
        self.frames = [pygame.transform.scale(frame, (64, 64)) for frame in self.original_frames]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = ""
        self.animation_counter = 0

    def update(self):
        self.animation_counter += 1
        if self.animation_counter % 5 == 0:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
            self.animation_counter = 0

        if self.direction == "RIGHT" and self.rect.right < 832 and map_layout[self.rect.y // 32][
            (self.rect.x + 32) // 32] != 1:
            self.rect.x += 32
        elif self.direction == "LEFT" and self.rect.left > 0 and map_layout[self.rect.y // 32][
            (self.rect.x - 32) // 32] != 1:
            self.rect.x -= 32
        elif self.direction == "UP" and self.rect.top > 0 and map_layout[(self.rect.y - 32) // 32][
            self.rect.x // 32] != 1:
            self.rect.y -= 32
        elif self.direction == "DOWN" and self.rect.bottom < 896 and map_layout[(self.rect.y + 32) // 32][
            self.rect.x // 32] != 1:
            self.rect.y += 32

    def change_direction(self, direction):
        self.direction = direction
        if direction == "RIGHT":
            self.frames = [pygame.transform.rotate(pygame.transform.scale(frame, (64, 64)), 0) for frame in
                           self.original_frames]
        elif direction == "LEFT":
            self.frames = [pygame.transform.rotate(pygame.transform.scale(frame, (64, 64)), 180) for frame in
                           self.original_frames]
        elif direction == "UP":
            self.frames = [pygame.transform.rotate(pygame.transform.scale(frame, (64, 64)), 90) for frame in
                           self.original_frames]
        elif direction == "DOWN":
            self.frames = [pygame.transform.rotate(pygame.transform.scale(frame, (64, 64)), 270) for frame in
                           self.original_frames]
        self.image = self.frames[self.frame_index]

    def draw(self, screen):
        offset = (64 - 32) // 2
        screen.blit(self.image, (self.rect.x - offset, self.rect.y - offset))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(orange_enemy_img, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.is_scared = False

    def update(self, player_x, player_y, power_mode):
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        random.shuffle(directions)

        self.is_scared = power_mode
        if self.is_scared:
            self.image = pygame.transform.scale(blue_enemy_img, (32, 32))
            player_x, player_y = -player_x, -player_y  # Reverse direction
        else:
            self.image = pygame.transform.scale(orange_enemy_img, (32, 32))

        if random.random() < 0.8:  # 80% chance to follow (or run away from) the player
            if self.rect.x < player_x and map_layout[self.rect.y // 32][(self.rect.x + 32) // 32] != 1:
                self.rect.x += 32
            elif self.rect.x > player_x and map_layout[self.rect.y // 32][(self.rect.x - 32) // 32] != 1:
                self.rect.x -= 32
            elif self.rect.y < player_y and map_layout[(self.rect.y + 32) // 32][self.rect.x // 32] != 1:
                self.rect.y += 32
            elif self.rect.y > player_y and map_layout[(self.rect.y - 32) // 32][self.rect.x // 32] != 1:
                self.rect.y -= 32
        else:
            for direction in directions:
                if direction == 'UP' and self.rect.y - 32 >= 0 and map_layout[self.rect.y // 32 - 1][self.rect.x // 32] != 1:
                    self.rect.y -= 32
                    break
                elif direction == 'DOWN' and self.rect.y + 32 < 896 and map_layout[self.rect.y // 32 + 1][self.rect.x // 32] != 1:
                    self.rect.y += 32
                    break
                elif direction == 'LEFT' and self.rect.x - 32 >= 0 and map_layout[self.rect.y // 32][self.rect.x // 32 - 1] != 1:
                    self.rect.x -= 32
                    break
                elif direction == 'RIGHT' and self.rect.x + 32 < 832 and map_layout[self.rect.y // 32][self.rect.x // 32 + 1] != 1:
                    self.rect.x += 32
                    break

    def reset_position(self):
        self.rect.topleft = (random.randint(8, 10) * 32, random.randint(8, 10) * 32)
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])


player = Player(32, 32)
enemies = [Enemy(random.randint(8, 10) * 32, random.randint(8, 10) * 32) for _ in range(4)]  # Spawn enemies in a range
food_positions = [(x * 32, y * 32) for y in range(len(map_layout)) for x in range(len(map_layout[y])) if map_layout[y][x] == 0]
power_pellet_positions = random.sample(food_positions, 5)  # Add 5 power pellets
score = 0
lives = 3
power_mode = False
power_mode_timer = 0

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(*enemies)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.change_direction("RIGHT")
            elif event.key == pygame.K_LEFT:
                player.change_direction("LEFT")
            elif event.key == pygame.K_UP:
                player.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                player.change_direction("DOWN")

    player.update()

    for enemy in enemies:
        enemy.update(player.rect.x, player.rect.y, power_mode)

    player_pos = (player.rect.x, player.rect.y)
    if player_pos in food_positions:
        food_positions.remove(player_pos)
        score += 10
    if player_pos in power_pellet_positions:
        power_pellet_positions.remove(player_pos)
        power_mode = True
        power_mode_timer = pygame.time.get_ticks()

    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            if power_mode:
                enemy.reset_position()
                score += 100
            else:
                lives -= 1
                player.rect.topleft = (32, 32)
                for enemy in enemies:
                    enemy.reset_position()
                if lives == 0:
                    running = False

    if power_mode and pygame.time.get_ticks() - power_mode_timer > 5000:
        power_mode = False

    screen.fill((0, 0, 0))
    for row in range(len(map_layout)):
        for col in range(len(map_layout[row])):
            if map_layout[row][col] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (col * 32, row * 32, 32, 32))
    for food in food_positions:
        pygame.draw.circle(screen, (255, 255, 0), (food[0] + 16, food[1] + 16), 8)
    for pellet in power_pellet_positions:
        pygame.draw.circle(screen, (255, 0, 0), (pellet[0] + 16, pellet[1] + 16), 8)  # Red power pellets

    for sprite in all_sprites:
        if isinstance(sprite, Player):
            sprite.draw(screen)
        else:
            screen.blit(sprite.image, sprite.rect.topleft)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (700, 10))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()


