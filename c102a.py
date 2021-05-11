import cv2
import dropbox
import time 
import random

starttime.time()
def TakeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        print(ret)
        imgName='img'+str(number)+'.png'
        cv2.imwrite(imgName,frame)
        starttime=time.time
        result=False
    return imgName
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def UploadFile(imgName):
    accessToken=""
    file=imgName
    filefrom =file
    fileto='/newFolder/'+imgName
    dbx=dropbox.Dropbox(accessToken)
    with open(filefrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.override)
        print('file uploaded')

def main():
    while(True):
        if((time.time()-starttime)>=300):
            name=TakeSnapshot()
            UploadFile(name)

main()