import cv2
camera_capture=cv2.VideoCapture(0)  #0 refer to camera device index
##fps=camera_capture.get(cv2.CAP_PROP_FPS)
##size = (int(camera_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
## int(camera_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
##video=cv2.VideoWriter("img.avi",cv2.VideoWriter_fourcc('I','4','2','0'), 
##fps, size)
success,frame=camera_capture.read()
camera_capture.release()
cv2.imwrite("img.png",frame)
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
lap=cv2.Laplacian(frame,-1,ksize=3)
sobel_x=cv2.Sobel(frame,-1,1,0)
sobel_y=cv2.Sobel(frame,-1,0,1)
com_sobel=cv2.bitwise_or(sobel_x,sobel_y)
canny=cv2.Canny(frame,100,200)
cv2.imshow("gray",gray)
cv2.imshow("img",frame)
cv2.imshow("lap",lap)
cv2.imshow("x",sobel_x)
cv2.imshow("y",sobel_y)
cv2.imshow("com_sobel",com_sobel)
cv2.imshow("canny",cv2.bitwise_not(canny)) #bit wise not to swap black and white
cv2.waitKey()
cv2.destroyAllWindows()
