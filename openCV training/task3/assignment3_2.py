import cv2
def canny_webcam():
    cap = cv2.VideoCapture(0)

    while(True):
        ret, video = cap.read()
        edge = cv2.Canny(video, 100, 200)
        cv2.imshow('pencil_sketch_video', edge)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
canny_webcam()



        
    


