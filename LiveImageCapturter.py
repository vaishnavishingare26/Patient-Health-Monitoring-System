
import cv2
import os

def getLiveImage():
        
        
          
    cap=cv2.VideoCapture(0)#2 for External Camera and 0 for System Camera
    count=0
    
    
    while cap.isOpened():
        _,capimg=cap.read()
        count=count+1
        if(count==50):
                
            
            cv2.imshow('Patient Live Image Capturer',capimg)
            cv2.imwrite("Captured_Images\Temp.jpg",capimg)
               
            print("Patient Live Image  is Captured")
            break  
                        
                  
        
    
    cap.release()
    cv2.destroyAllWindows()
    return 1