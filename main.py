import pygame
import sys
import pygame.image
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


player = None

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(0 ,len(level), 1):
        for x in range(0, len(level[y]), 1):
            if level[y][x] == '.':
                screen.blit(tile_images['empty'], (x * 50, y * 50))
                Tile('empty', x, y)
            elif level[y][x] == '#':
                screen.blit(tile_images['wall'], (x * 50, y * 50))
                Tile('wall', x, y)
            elif level[y][x] == '@':
                screen.blit(tile_images['empty'], (x * 50, y * 50))
                screen.blit(player_image, (x * 50, y * 50))
                new_player = Player(x, y)
    return new_player, x, y


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    player, level_x, level_y = generate_level(load_level('map.txt'))
    clock = pygame.time.Clock()
    print('test')
    running = True

    FPS = 50

    while running:
        generate_level('map.png')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
