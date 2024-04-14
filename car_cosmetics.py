"""
MIT License

Copyright (c) 2024 D14rn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import pygame


class Bumper(pygame.Rect):
    def __init__(self, car):
        self.car = car
        super().__init__(self.coordinates[2][0], self.coordinates[2][1] - self.height // 2, self.width, self.height)

    @property
    def headlights_coordinates(self):
        coords = self.coordinates
        return {
            "left": (
                coords[2][0] + self.width // 6,
                coords[2][1] - self.height // 2
                ),
            "right": (
                coords[3][0] - self.width // 6,
                coords[3][1] - self.height // 2
                ),
        }

    @property
    def coordinates(self):
        car = self.car
        bumper_height = self.height
        front_offset = car.width // 10

        return [
            (car.x + front_offset, car.y - bumper_height), # top left
            (car.x + car.width - front_offset, car.y - bumper_height), # top right
            (car.x, car.y), # bottom left
            (car.x + car.width, car.y) # bottom right
        ]
    
    @property
    def height(self):
        return self.car.length // 10

    @property
    def width(self):
        return self.car.width


class Headlight(pygame.Rect):
    def __init__(self, x_pos, y_pos, diameter):
        super().__init__(x_pos, y_pos, diameter, diameter)

    @classmethod
    def create_headlights(cls, bumper):
        coords = bumper.headlights_coordinates
        return (
            cls.create_headlight(bumper, coords["left"][0], coords["left"][1]),
            cls.create_headlight(bumper, coords["right"][0], coords["right"][1])
        )

    @classmethod
    def create_headlight(cls, bumper, x_pos, y_pos):
        diameter = bumper.height // 3
        return cls(x_pos, y_pos, diameter)

    # @classmethod
    # def create_left_headlight(cls, bumper):
    #     x_pos = bumper.x + bumper.width // 6
    #     return cls.create_headlight(bumper, x_pos)

    # @classmethod
    # def create_right_headlight(cls, bumper):
    #     x_pos = bumper.x + bumper.width // 6 * 5
    #     return cls.create_headlight(bumper, x_pos)
