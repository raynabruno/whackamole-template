import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        screen = pygame.display.set_mode((640, 512))


        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft=(random.randrange(0, 640 - mole_image.get_width()), random.randrange(0, 512 - mole_image.get_height())))


        clock = pygame.time.Clock()
        running = True


        #Starting coordinates
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mole_x <= mouse_x <= mole_x + 32 and mole_y <= mouse_y <= mole_y + 32:
                        mole_x, mole_y = random.randrange(0,640), random.randrange(0,512)
                        mole_x = mole_x-mole_x%32
                        mole_y = mole_y-mole_y%32



            screen.fill("light green")
            for y in range(16):
                pygame.draw.line(screen, "black", (0,y*32), (640, y*32))
            for x in range(20):
                pygame.draw.line(screen, "black", (x * 32, 0), (x * 32, 640))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


# pygame.draw.line(screen,color, (x1,y1),(x2,y2))

if __name__ == "__main__":
    main()
