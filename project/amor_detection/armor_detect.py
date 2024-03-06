from Armor import *

class Detector:
    def __init__(self, detect_color) -> None:
        self.detect_color = detect_color
        self.params = params()

    def detect(self, frame):
        binary_img = self.preprocess(frame)
        cv2.imshow('binary_img', binary_img)
        lights = self.findLights(binary_img, frame)
        for light in lights:
            if light.color == "blue":
                cv2.line(frame, light.top.astype(int), light.bottom.astype(int), (255, 0, 0), 2)
            elif light.color == "red":
                cv2.line(frame, light.top.astype(int), light.bottom.astype(int), (0, 0, 255), 2)
        armors = self.matchLights(lights)
        return armors

    def preprocess(self, frame):
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary_img = cv2.threshold(gray_img, self.params.binary_threshold, 255, cv2.THRESH_BINARY)
        return binary_img

    def findLights(self, binary_img, frame):
        lights = []
        contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if contour.size < 10:
                continue
            rect = cv2.minAreaRect(contour)
            if cv2.boxPoints(rect).any() < 0:
                continue
            light = Light(rect)
            if self.isLight(light):
                l_rect = cv2.boundingRect(light.points)
                cv2.putText(frame, str(round(light.angle, 2)), (int(light.center[0]) + 10, int(light.center[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                cv2.putText(frame, str(round(light.length, 2)), (int(light.bottom[0]) + 10, int(light.bottom[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                if l_rect[0] > 0 and l_rect[1] > 0 and l_rect[0] + l_rect[2] < frame.shape[1] and l_rect[1] + l_rect[3] < frame.shape[0]:
                    sum_r = 0
                    sum_b = 0
                    roi = frame[l_rect[1]:l_rect[1] + l_rect[3], l_rect[0]:l_rect[0] + l_rect[2]]
                    for i in range(roi.shape[0]):
                        for j in range(roi.shape[1]):
                            sum_r += roi[i][j][2]
                            sum_b += roi[i][j][0]
                    if sum_r > sum_b:
                        light.color = "red"
                    else:
                        light.color = "blue"
                    cv2.putText(frame, light.color, (l_rect[0], l_rect[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                    lights.append(light)
        return lights

    def isLight(self, light: Light):
        ratio = light.width / light.length
        ratio_ok = self.params.light_min_ratio < ratio and ratio < self.params.light_max_ratio
        angle_ok = light.angle < self.params.light_max_angle
        return ratio_ok and angle_ok

    def matchLights(self, lights):
        armors = []
        used_lights = []
        for i in range(len(lights)):
            if lights[i] in used_lights:
                continue
            for j in range(i + 1, len(lights)):
                if lights[i].color != self.detect_color or lights[j].color != self.detect_color:
                    continue
                if self.containLight(lights[i], lights[j], lights):
                    continue
                if self.isArmor(lights[i], lights[j]):
                    armor = Armor(lights[i], lights[j])
                    used_lights.append(lights[i])
                    used_lights.append(lights[j])
                    armors.append(armor)
        return armors

    def containLight(self, light_1: Light, light_2: Light, lights: list):
        points = np.array([light_1.top, light_1.bottom, light_2.top, light_2.bottom])
    
        for light in lights:
            if np.all(light.center == light_1.center) or np.all(light.center == light_2.center):
                continue
            if cv2.pointPolygonTest(points, light.center, False) > 0 or \
                cv2.pointPolygonTest(points, light.top, False) > 0 or \
                    cv2.pointPolygonTest(points, light.bottom, False) > 0:
                return True
        return False

    def isArmor(self, light_1: Light, light_2: Light):
        light_length_ratio = light_1.length / light_2.length if light_1.length < light_2.length else light_2.length / light_1.length
        light_length_ratio_ok = light_length_ratio > self.params.armor_min_light_length_ratio

        avg_light_length = (light_1.length + light_2.length) / 2
        center_distance = cv2.norm(light_1.center - light_2.center) / avg_light_length
        center_distance_ok = center_distance >= self.params.armor_min_center_distance and center_distance < self.params.armor_max_center_distance

        diff = light_1.center - light_2.center
        angle = math.atan2(abs(diff[1]), abs(diff[0])) / math.pi * 180
        angle_ok = angle < self.params.armor_max_angle
        return light_length_ratio_ok and center_distance_ok and angle_ok

if __name__ == "__main__":
    detect_color = "blue"
    det = Detector(detect_color)

    # img = cv2.imread("./images/rm.jpg")
    # armors = det.detect(img)
    # for armor in armors:
    #     cv2.line(img, armor.left_light.top.astype(int), armor.right_light.bottom.astype(int), (0, 255, 0), 2)
    #     cv2.line(img, armor.left_light.bottom.astype(int), armor.right_light.top.astype(int), (0, 255, 0), 2)
    #     cv2.putText(img, str(round(armor.angle, 2)), (int(armor.center[0]) + 10, int(armor.center[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    # cv2.imshow('frame', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            armors = det.detect(frame)
            for armor in armors:
                cv2.line(frame, armor.left_light.top.astype(int), armor.right_light.bottom.astype(int), (0, 255, 0), 3)
                cv2.line(frame, armor.left_light.bottom.astype(int), armor.right_light.top.astype(int), (0, 255, 0), 3)
                cv2.putText(frame, str(round(armor.angle, 2)), (int(armor.center[0]) + 10, int(armor.center[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == 27:
                break
    cv2.destroyAllWindows()
    cap.release()