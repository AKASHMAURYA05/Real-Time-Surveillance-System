import cv2, sys, numpy, os, time
def capturing():
    count = 0
    size = 4
    fn_haar = 'haarcascade_frontalface_default.xml'
    fn_dir = 'database'
    fn_name = input("Enter the Name of the Person:-")
    path = os.path.join(fn_dir, fn_name)
    
    # print(path)
    if not os.path.isdir(path):
        os.mkdir(path)
    (im_width, im_height) = (112, 92)
    haar_cascade = cv2.CascadeClassifier(fn_haar)
    webcam = cv2.VideoCapture(0)

    print("capturing Going On")
    while count <30:
        _,image = webcam.read()
        
        # cv2.imshow("image",image)
        image = cv2.flip(image, 1, 0)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # cv2.imshow("gray",gray)
        mini = cv2.resize(gray,(gray.shape[1]//size, gray.shape[0]//size))
        
        # cv2.imshow("mini",faces)
        faces = haar_cascade.detectMultiScale(mini)
        faces = sorted(faces, key=lambda x: x[3])
        if faces:
            face_i = faces[0]
            (x, y, w, h) = [v * size for v in face_i]
            face = gray[y:y + h, x:x + w]
            
            # cv2.imshow("face",face)

            face_resize = cv2.resize(face, (im_width, im_height))
            pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path)
                if n[0]!='.' ]+[0])[-1] + 1
            cv2.imwrite('%s/%s.png' % (path, pin), face_resize)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(image, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
                1,(0, 255, 0))
            time.sleep(0.38)
            count += 1
        cv2.imshow('OpenCV', image)
        key = cv2.waitKey(10)
        if key == 27:
            break
    print(str(count) + " images taken and saved to " + fn_name +" folder in database ")