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
