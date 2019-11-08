import dlib
import cv2
import imutils
import math
import time

# Camera resolution, recommended ratio 16:9
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480


class FACE(object):
    def __init__(self):
        import numpy
        self.cap = cv2.VideoCapture(0)
        self.time_start = time.time()

        # show and set camera stat
        self.cap.set(3,CAMERA_WIDTH)
        self.cap.set(4,CAMERA_HEIGHT)
        self.sizew = self.cap.get(3)
        self.sizeh = self.cap.get(4)
        print(self.sizew,self.sizeh)
        self.detector = dlib.get_frontal_face_detector()
        self.xCenter = 320
        self.yCenter = 240
    
    def getCap(self):
        return self.cap.isOpened()
    
    def endCam(self):
        self.cap.release()
        cv2.destroyAllWindows()
    
    def observe(self):
        ret, frame = self.cap.read()
        face_rects, scores, idx = self.detector.run(frame, 0)
        self.time_end = time.time()
            # flip video
            # frame_flip = cv2.flip(frame, 1)

        faceS0 = 0
        #read data
        for i, d in enumerate(face_rects):
            x1 = d.left()
            y1 = d.top()
            x2 = d.right()
            y2 = d.bottom()
            faceS = (y2-y1)*(x2-x1)
            text = "%2.2f(%d)" % (scores[i], idx[i])

            #show center position
            if faceS > faceS0:
                self.xCenter = int((x1 + x2)/2)
                self.yCenter = int((y1 + y2)/2)
            print("(", self.xCenter, ", ", self.yCenter, ")",self.time_end-self.time_start)
            cv2.circle(frame, (self.xCenter, self.yCenter), int(math.log(self.sizew + self.sizeh)), (255, 0, 0), -1)
    

            # Mark human face
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)

            # show the score
            cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,
                    0.7, (255, 255, 255), 1, cv2.LINE_AA)

        # show the result
        cv2.imshow("Face Detection", frame)

    def getxCenter(self):
        return self.xCenter

    def getyCenter(self):
        return self.yCenter
