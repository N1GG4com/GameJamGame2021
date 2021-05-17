import pygame
import sys
import random


def create_block():
    #creates variables that set x and y for a new block
    random_block_pos = random.choice(blockHeight)
    random_block_pos2 = random.choice(blockHeight2)
    #block types
    lower_block = block_surface.get_rect(midtop = (1000, random_block_pos))
    mid_block = block_surface.get_rect(midtop = (1000, 540))
    upper_block = block_surface.get_rect(midtop = (1000, random_block_pos2))
    return  upper_block, lower_block, mid_block
def draw_floor():
    screen.blit(floor, (floor_x_pos, 0))
    screen.blit(floor, (floor_x_pos + 1280, 0))


def move_blocks(blocks):
    for block in blocks:
        block.centerx -= 5
    return blocks


def draw_blocks(blocks):
    for block in blocks:
        screen.blit(block_surface, block)


def colisionCheck(blocks):
    for block in blocks:
        if player_rect.colliderect(block):
            player_rect.clamp_ip(blockList)
    if player_rect.top <= -100 or player_rect.bottom >= 520:
        player_rect.clamp_ip(floor_rect)


pygame.init()

gravity = 0.65
playerMovement = 0
clock = pygame.time.Clock()
FPS = 75

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("The Never Ending Story")

bg = pygame.image.load('Assets/Sunny-land-assets-files/PNG/environment/layers/back.png').convert()
bg = pygame.transform.scale((bg), (1280, 720))

floor = pygame.image.load('Assets/Untitled.png')
floor_x_pos = 0
floor_rect = pygame.Rect((100, 67), (0, 540))

player = pygame.image.load('Assets/Adventurer-1/Individual Sprites/adventurer-idle-01.png')
player = pygame.transform.scale(player, (200, 148))
player_rect = player.get_rect(center = (100, 540))

block_surface = pygame.image.load('Assets/Sunny-land-assets-files/PNG/environment/props/block-big.png')
block_surface = pygame.transform.scale2x(block_surface)
blockList = []
blockHeight = [484, 540]
blockHeight2 = [428, 484, 540]
SPAWNBLOCK = pygame.USEREVENT
pygame.time.set_timer(SPAWNBLOCK, 1200)


while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 playerMovement = 0
                 playerMovement -= 9
        if event.type == SPAWNBLOCK:
            blockList.extend(create_block())
    screen.blit(bg, (0, 0))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -1280:
        floor_x_pos = 0
    screen.blit(floor, (floor_x_pos, 0))
    screen.blit(player, player_rect)

    playerMovement += gravity
    player_rect.centery += playerMovement
    colisionCheck(blockList)
    blockList = move_blocks(blockList)
    draw_blocks(blockList)
    pygame.display.update()
    clock.tick(FPS)