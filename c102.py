import cv2

def TakeSnapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        print(ret)
        cv2.imwrite('new.jpg',frame)
        result=False

    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
TakeSnapshot()