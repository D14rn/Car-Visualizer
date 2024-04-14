import pygame
from visualizer import *


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Car Visualizer")
    clock = pygame.time.Clock()
    running = True
    car = Car(WIDTH // 2, HEIGHT // 2, 400, 200, body_width=5)
    car_controller = CarController(car)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        car_controller.update(keys)

        screen.fill(BLACK)
        car.draw(screen)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
