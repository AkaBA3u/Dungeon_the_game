import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    window = pygame.display.set_mode(size)
    fps = 60
    clock = pygame.time.Clock()
    print('test')

    running = True

    while running:
        window.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.MOUSEMOTION:
                pass
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()