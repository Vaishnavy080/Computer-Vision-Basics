import cv2
img = cv2.imread("sample.jpg")
img2=cv2.imread("download.jpg")             #reads the image using opencv libraries
cv2.imshow("First CV program",img)          #displays the image read
cv2.imwrite("logo.jpg",img2)                #writes an image
cv2.waitKey(0)                              #wait command for delaying the display time
cv2.destroyAllWindows()
