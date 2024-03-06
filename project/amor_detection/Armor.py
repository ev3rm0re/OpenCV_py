import cv2
import numpy as np
import math

class params:
    def __init__(self):
        self.binary_threshold = 220
        self.light_max_angle = 30
        self.light_min_ratio = 0.1
        self.light_max_ratio = 0.5

        self.armor_min_light_length_ratio = 0.75
        self.armor_min_center_distance = 1.0
        self.armor_max_center_distance = 3.5
        self.armor_max_angle = 30

class Light:
    def __init__(self, rect):
        center, size, angle = rect
        self.points = np.array(sorted(cv2.boxPoints(rect), key=lambda x: x[1]))
        self.center = np.array(center)
        self.top = (self.points[0] + self.points[1]) / 2
        self.bottom = (self.points[2] + self.points[3]) / 2

        self.length = cv2.norm(self.top - self.bottom)
        self.width = cv2.norm(self.points[0] - self.points[1])

        self.angle = 90 - math.atan2(abs(self.top[1] - self.bottom[1]), abs(self.top[0] - self.bottom[0])) * 180 / math.pi

class Armor:
    def __init__(self, light1, light2):
        self.left_light = light1 if light1.center[0] < light2.center[0] else light2
        self.right_light = light1 if light1.center[0] > light2.center[0] else light2
        self.center = (self.left_light.center + self.right_light.center) / 2
        self.angle = abs(math.atan2(self.left_light.center[1] - self.right_light.center[1], self.left_light.center[0] - self.right_light.center[0])) * 180 / math.pi

if __name__ == "__main__":
    pass