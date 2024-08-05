import cv2 
import winsound
def full_frame():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()
        
        # print(frame1)
        # print(frame2)
        
        diff = cv2.absdiff(frame2, frame1)
        
        # print(diff)
        
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        # print(diff)
        
        diff = cv2.blur(diff, (5,5))
        
        # print(diff)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contr, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)
            
            print(max_cnt)
            
            x,y,w,h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
            winsound.Beep(500, 50)

        else:
            
            cv2.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)

        cv2.imshow("Full Frame", frame1)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

