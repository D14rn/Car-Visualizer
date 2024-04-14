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

from math import radians
import pygame
from wheel import Wheel
from constants import RED, YELLOW
from car_cosmetics import Bumper, Headlight


class Car:
    def __init__(self, x, y, length, width, body_width=1, color=RED) -> None:
        self.x = x - width // 2
        self.y = y - length // 2
        self.length = length
        self.width = width
        self.body_width = body_width
        self.color = color
        self._wheels = self.create_wheels()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.length)
        self.bumper = Bumper(self)
        self.headlights = [Headlight.create_left_headlight(self.bumper), Headlight.create_right_headlight(self.bumper)]

    @property
    def front_wheels(self):
        return list(self._wheels["front_wheels"].values())
    
    @property
    def back_wheels(self):
        return list(self._wheels["back_wheels"].values())

    @property
    def wheels(self):
        return self.front_wheels + self.back_wheels

    def turn_right(self):
        self.turn(Wheel.turn_right)

    def turn_left(self):
        self.turn(Wheel.turn_left)

    def turn_reset(self):
        self.turn(Wheel.turn_reset)
    
    def turn(self, func):
        self.func_to_all(self.front_wheels, func)
    
    @staticmethod
    def func_to_all(arr, func):
        for elem in arr:
            func(elem)

    def go_forward(self):
        self.func_to_all(self.wheels, Wheel.go_forward)
    
    def go_backward(self):
        self.func_to_all(self.wheels, Wheel.go_backward)

    def create_wheels(self):
        wheel_length = self.length // 4
        wheel_width = self.width // 4
        fw_ypos = self.y + self.length//4 - wheel_length//2
        bw_ypos = self.y + self.length//4*3 - wheel_length//2
        lw_xpos = self.x - wheel_width//2
        rw_xpos = self.x + self.width - wheel_width//2

        front_wheels = {
            "left": Wheel(lw_xpos, fw_ypos, wheel_length, wheel_width),
            "right": Wheel(rw_xpos, fw_ypos, wheel_length, wheel_width)
        }

        back_wheels = {
            "left": Wheel(lw_xpos, bw_ypos, wheel_length, wheel_width),
            "right": Wheel(rw_xpos, bw_ypos, wheel_length, wheel_width)
        }

        return {
            "front_wheels": front_wheels,
            "back_wheels": back_wheels
        }

    def draw_wheels(self, screen):
        for wheel in self.wheels:
            if isinstance(wheel, Wheel):
                wheel.draw(screen)
    
    def draw_body(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, width=self.body_width)
    
    def draw_bumper(self, screen):
        pygame.draw.arc(screen, self.color, self.bumper, 0, radians(180), width=20)
    
    def draw_headlights(self, screen):
        for headlight in self.headlights:
            pygame.draw.circle(screen, YELLOW, (headlight.x, headlight.y), headlight.width)

    def draw(self, screen):
        self.draw_body(screen)
        self.draw_bumper(screen)
        self.draw_headlights(screen)
        self.draw_wheels(screen)


class CarController:
    def __init__(self, car: Car) -> None:
        self.car = car

    def update(self, keys):
        if keys[pygame.K_z]:
            self.car.go_forward()
        elif keys[pygame.K_s]:
            self.car.go_backward()

        if keys[pygame.K_q]:
            self.car.turn_left()
        elif keys[pygame.K_d]:
            self.car.turn_right()
        else:
            self.car.turn_reset()
