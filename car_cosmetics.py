import pygame

class Bumper(pygame.Rect):
    def __init__(self, car):
        bumper_height = car.length // 10
        super().__init__(car.x, car.y - bumper_height // 2, car.width, bumper_height)


class Headlight(pygame.Rect):
    def __init__(self, x_pos, y_pos, diameter):
        super().__init__(x_pos, y_pos, diameter, diameter)

    @classmethod
    def create_left_headlight(cls, bumper):
        x_pos = bumper.x + bumper.width // 6
        return cls.create_headlight(bumper, x_pos)

    @classmethod
    def create_right_headlight(cls, bumper):
        x_pos = bumper.x + bumper.width // 6 * 5
        return cls.create_headlight(bumper, x_pos)

    @classmethod
    def create_headlight(cls, bumper, x_pos):
        y_pos = bumper.y + bumper.height // 3
        return cls(x_pos, y_pos, bumper.height // 3)