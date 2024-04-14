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


from math import sin, cos, radians, pi
import pygame
from .constants import *


class Wheel:
    def __init__(self, x, y, length, width, speed=20, turn_ratio=1, color=DARK_GREY) -> None:
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.angle = 0
        self.speed = speed
        self.turn_ratio = 0.75
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.length)
        self.marker = WheelMarker(self, AQUAMARINE_BLUE)

    @property
    def center_y(self):
        return self.y + self.length / 2

    def turn(self, angle):
        self.angle = min(max(angle * self.turn_ratio, -90), 90)

    def turn_right(self):
        self.turn(-45)

    def turn_left(self):
        self.turn(45)

    def turn_reset(self):
        self.turn(0)
    
    def go_forward(self):
        self.marker.move_forward()
    
    def go_backward(self):
        self.marker.move_backward()
    
    @staticmethod
    def draw_rotated_rect(screen, color, rect, angle):
        rotated_surface = pygame.Surface(rect.size)
        rotated_surface.set_colorkey(BLACK)
        rotated_surface.fill(color)

        rotated_surface = pygame.transform.rotate(rotated_surface, angle)

        rotated_rect = rotated_surface.get_rect(center=rect.center)

        screen.blit(rotated_surface, rotated_rect.topleft)

    def draw(self, screen):
        self.draw_rotated_rect(screen, self.color, self.rect, self.angle)
        if self.marker.is_drawable(): 
            self.draw_rotated_rect(screen, self.marker.color, self.marker.rect, self.angle)


class WheelMarker:
    def __init__(self, wheel: Wheel, color=RED) -> None:
        self.wheel = wheel
        self._stage = 90
        self.color = color

    def is_drawable(self):
        return self.stage < 180

    @property
    def x(self):
        x_center_wheel = self.wheel.x
        x_translation = self.current_radius * cos(radians(self.wheel.angle + 90 + 180))
        return x_center_wheel + x_translation

    @property
    def current_radius(self):
        return (self.wheel.length / 2) * cos(radians(self.stage))

    @property
    def y(self):
        y_center_wheel = self.wheel.center_y - self.length / 2
        y_translation = self.current_radius * sin(radians(self.wheel.angle + 90))
        return y_center_wheel + y_translation

    @property
    def length(self):
        ratio = sin(radians(self.stage)) / 6
        return self.wheel.length * ratio

    @property
    def width(self):
        return self.wheel.width

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.length)
    
    @property
    def stage(self):
        return self._stage
    
    @stage.setter
    def stage(self, value):
        self._stage = value % 360

    def move_forward(self):
        self.stage += self.wheel.speed

    def move_backward(self):
        self.stage -= self.wheel.speed
