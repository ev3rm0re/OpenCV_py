import cv2

class Tracker:
    def __init__(self):
        self.trackers = cv2.legacy.MultiTracker.create()
        self.active_tracks = []

    def track(self, frame):
        mask = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(mask, 120, 255, cv2.THRESH_BINARY)
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # 定义新的目标列表
        new_targets = []

        # 更新跟踪器中的目标
        for cnt in contours:
            if cv2.contourArea(cnt) > 4000:
                bbox = cv2.boundingRect(cnt)
                if not self.is_inside_existing(bbox):
                    tracker = cv2.legacy.TrackerMOSSE.create()
                    self.trackers.add(tracker, frame, bbox)
                    new_targets.append(bbox)

        # 更新跟踪器状态
        if len(self.active_tracks) > 0:
            success, boxes = self.trackers.update(frame)
            if success:
                self.active_tracks = boxes

        # 返回更新后的目标框和新出现的目标框
        return frame, self.active_tracks, new_targets

    def delete(self):
        self.trackers.clear()

    def is_inside_existing(self, bbox):
        # 判断bbox是否在已有的跟踪目标中
        for track in self.active_tracks:
            x, y, w, h = track
            if x <= bbox[0] <= x+w and y <= bbox[1] <= y+h:
                return True
        return False

if __name__ == "__main__":
    tracker = Tracker()
    cap = cv2.VideoCapture("F:/items/Archive01/OpenCV_py/project/bulletcount/video.mp4")
    bullet_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame, active_tracks, new_targets = tracker.track(frame)

        # 绘制新出现的目标
        for bbox in new_targets:
            x, y, w, h = [int(i) for i in bbox]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            # 每检测到一个新目标，子弹数加1
            bullet_count += 1

        cv2.putText(frame, "Bullet count: {}".format(bullet_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(10) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    tracker.delete()
    print("Bullet count: ", bullet_count)