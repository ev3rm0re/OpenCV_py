import cv2
import numpy as np
import math


l_max_angle = 45
l_min_ratio = 0.1
l_max_ratio = 0.3
a_min_light_length_ratio = 0.75
a_min_center_distance = 2.0
a_max_center_distance = 5.0
a_max_angle = 45

class Light():
    def __init__(self, rect: cv2.RotatedRect):
        self.p = sorted(cv2.boxPoints(rect), key=lambda point: point[1])
        self.center = np.array([rect[0][0], rect[0][1]]).astype(int)
        self.top = ((self.p[0] + self.p[1]) / 2).astype(int)
        self.bottom = ((self.p[2] + self.p[3]) / 2).astype(int)

        self.length = cv2.norm(self.top - self.bottom)
        self.width = cv2.norm(self.p[0] - self.p[1])

        self.angle = math.atan2(abs(self.top[0] - self.bottom[0]), abs(self.top[1] - self.bottom[1])) / math.pi * 180
        self.color: str

class Armor():
    def __init__(self, light_1: Light, light_2: Light):
        self.left_light = light_1 if light_1.center[0] < light_2.center[0] else light_2
        self.right_light = light_1 if light_1.center[0] > light_2.center[0] else light_2
        self.center = (light_1.center + light_2.center) / 2

class Detector:
    def __init__(self, detect_color) -> None:
        self.detect_color = detect_color

    def detect(self, frame):
        binary_img = self.preprocess(frame)
        cv2.imshow('binary_img', binary_img)
        lights = self.findLights(binary_img, frame)
        print(len(lights))
        armors = self.matchLights(lights)
        return armors

    def preprocess(self, frame):
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary_img = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY)
        return binary_img

    def findLights(self, binary_img, frame):
        lights = []
        contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if contour.size < 100:
                continue
            rect = cv2.minAreaRect(contour)
            light = Light(rect)
            if self.isLight(light):
                sum_r = 0
                sum_b = 0
                roi = frame[int(light.p[0][1]):int(light.p[3][1]), int(light.p[0][0]):int(light.p[3][0])]
                if roi.size != 0:
                    r, g, b = cv2.split(roi)
                    sum_r = np.sum(r)
                    sum_b = np.sum(b)
                    if sum_r > sum_b:
                        light.color = "red"
                    else:
                        light.color = "blue"
            lights.append(light)
        return lights

    def isLight(self, light: Light):
        ratio = light.width / light.length
        ratio_ok = l_min_ratio < ratio < l_max_ratio
        angle_ok = light.angle < l_max_angle
        return ratio_ok and angle_ok

    def matchLights(self, lights: list):
        armors = []
        for i in range(len(lights)):
            for j in range(i + 1, len(lights)):
                if lights[i].color != self.detect_color or lights[j].color != self.detect_color:
                    print(lights[i].color, lights[j].color)
                    print("color not match")
                    continue
                if self.containLight(lights[i], lights[j], lights):
                    print("contain light")
                    continue
                if self.isArmor(lights[i], lights[j]):
                    armor = Armor(lights[i], lights[j])
                    armors.append(armor)
        return armors

    def containLight(self, light_1: Light, light_2: Light, lights: list):
        points = np.array([light_1.p[0], light_1.p[1], light_1.p[2], light_1.p[3], light_2.p[0], light_2.p[1], light_2.p[2], light_2.p[3]])
        bounding_box = cv2.boundingRect(points)

        for light in lights:
            if light.center.all() == light_1.center.all() or light.center.all() == light_2.center.all():
                continue
            if bounding_box[0] < light.center[0] < bounding_box[0] + bounding_box[2] and bounding_box[1] < light.center[1] < bounding_box[1] + bounding_box[3]:
                return True
        return False

    def isArmor(self, light_1: Light, light_2: Light):
        light_length_ratio = light_1.length / light_2.length if light_1.length < light_2.length else light_2.length / light_1.length
        light_length_ratio_ok = light_length_ratio > a_min_light_length_ratio

        avg_light_length = (light_1.length + light_2.length) / 2
        center_distance = cv2.norm(light_1.center - light_2.center) / avg_light_length
        center_distance_ok = center_distance > a_min_center_distance and center_distance < a_max_center_distance

        diff = light_1.center - light_2.center
        angle = abs(math.atan2(diff[1], diff[0]) / math.pi * 180)
        angle_ok = angle < a_max_angle

        return light_length_ratio_ok and center_distance_ok and angle_ok

if __name__ == "__main__":
    detect_color = "blue"
    det = Detector(detect_color)
    cap = cv2.VideoCapture("http://192.168.8.199:4747/video?1920x1080")
    while True:
        ret, frame = cap.read()
        if ret:
            armors = det.detect(frame)
            for armor in armors:
                cv2.line(frame, armor.left_light.top, armor.right_light.top, (0, 255, 0), 3)
                cv2.line(frame, armor.left_light.bottom, armor.right_light.bottom, (0, 255, 0), 3)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == 27:
                break
    cv2.destroyAllWindows()
    cap.release()