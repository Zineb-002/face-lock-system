import cv2
import os


key = cv2. waitKey(1)
cam = cv2.VideoCapture(0)
path = 'img/'
image_name = 'Hasan'
while True:
    try:
        check, frame = cam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename=path +image_name+'.jpg', img=frame)
            cam.release()
            img_new = cv2.imread(path +image_name+'.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread(path+image_name+'.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 100x100 scale...")
            img_ = cv2.resize(gray,(100,100))
            print("Resized...")
            img_resized = cv2.imwrite(filename=path+image_name+'-final.jpg', img=img_)
            os.remove(path +image_name+'.jpg')
            print("Image saved!")
            break
        elif key == ord('q'):
            print("Turning off camera.")
            cam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Turning off camera.")
        cam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
