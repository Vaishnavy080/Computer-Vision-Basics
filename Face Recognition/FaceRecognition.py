import cv2
import os
alg = "J:\Python Projects\haarcascade_algos\haarcascade_frontalface_default.xml"                #imports the algo in the variable alg
haar = cv2.CascadeClassifier(alg)                                                               #loads the algo.xml file in the cv2 Cascade Classifier 
cam = cv2.VideoCapture(0)                                                                       #Initializes the camera
dataset = 'dataset'                                                                             
name = 'MyData'

path = os.path.join('J:\Python Projects\Computer Vision Basics\Face Recognition',dataset)       #A new folder "dataset" will be created in the given path      
if not os.path.isdir(path):
    os.mkdir(path)                                                                              #makes directory if not found
    
(width,height)=(130,100)                                                                        
count = 1                                                                                       #counter for the images captured
while (count<=30):
    print(count)
    (_,img)= cam.read()                                                                         #reads the images the camera captures
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                                              #converts the coloured image into gray
    faces = haar.detectMultiScale(grayImg,1.3,4)                                                
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)                                          #displays rectangles on the faces detected
        onlyFace = grayImg[y:y+h,x:x+w]                                                         #crops the face
        resizeImg = cv2.resize(onlyFace,(width,height))                                         #resizes the faces cropped, the greater the width,height,greater the distortion
        cv2.imwrite(os.path.join(dataset,"%s%s.jpg"%(name,count)),resizeImg)                    #stores images in the dataset folder created earlier 
        count += 1                                                                              
    cv2.imshow("Facedetection",img)                                                             #shows the camera window                               
    key = cv2.waitKey(10)
    if key == "27":
        break
print("Face captured successfully")
cam.release()                                                                                   
cv2.destroyAllWindows()
