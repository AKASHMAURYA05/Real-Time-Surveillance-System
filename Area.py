import winsound
import cv2 

top_left = False
bottom_right = False
x1,y1,x2,y2 = 0,0,0,0


def select_region(event, x, y, flag, param):
    global x1,x2,y1,y2,top_left, bottom_right
    if event == cv2.EVENT_LBUTTONDOWN:
        x1,y1 = x,y 
        top_left = True
    elif event == cv2.EVENT_RBUTTONDOWN:
        x2,y2 = x,y
        bottom_right = True    
        print("Top-Left point is selected :-----", top_left)
        print("\n")
        print("Bottom-Right point is selected :-----", bottom_right)

def Frame():

    global x1,x2,y1,y2, top_left, bottom_right
    cap = cv2.VideoCapture(0)
    
    cv2.namedWindow("select_region_region")
    cv2.setMouseCallback("select_region_region", select_region)

    while True:
        _, frame = cap.read()

        cv2.imshow("select_region_region", frame)

        if cv2.waitKey(1) == 27 or bottom_right == True:
            cv2.destroyAllWindows()
            print("Done Framing")
            break

    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        frame1only = frame1[y1:y2, x1:x2]
        frame2only = frame2[y1:y2, x1:x2]

        diff = cv2.absdiff(frame2only, frame1only)
        # cv2.imshow("diff",diff)
        
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("diff",diff)

        diff = cv2.blur(diff, (5,5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        # cv2.imshow("thresh",thresh)

        contr, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)
            # print(max_cnt)
            x,y,width,height = cv2.boundingRect(max_cnt)
            
            cv2.rectangle(frame1, (x+x1, y+y1), (x+width+x1, y+height+y1), (0,255,0), 2)
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)
            winsound.Beep(500, 50)

        else:
            cv2.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)

        cv2.rectangle(frame1, (x1,y1), (x2, y2), (0,0,255), 1)
        cv2.imshow("Monitoring in Frame", frame1)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break