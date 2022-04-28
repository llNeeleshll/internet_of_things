import cv2
import urllib.request
import numpy as np
 
url='http://192.168.29.34/1600x1200.jpg'
 
while True:

    try:
        img_resp=urllib.request.urlopen(url, timeout=5)
    except Exception as e:
        break

    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)

    img = cv2.resize(img, (700,500))   
 
    cv2.imshow("muon_live",img)
    #cv2.resizeWindow("muon_live", 700, 500)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 
 