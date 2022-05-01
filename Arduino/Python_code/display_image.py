import cv2
import urllib.request
import numpy as np
import torch
 
url='http://192.168.29.34/1600x1200.jpg'

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
 
while True:

    try:
        img_resp=urllib.request.urlopen(url, timeout=5)
    except Exception as e:
        break

    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)

    img = cv2.resize(img, (700,500))   

    results = model([img])

    df = results.pandas().xyxy[0]

    for item in df.iterrows():
        x1 = int(item[1]['xmin'])
        x2 = int(item[1]['xmax'])
        y1 = int(item[1]['ymin'])
        y2 = int(item[1]['ymax'])

        name = item[1]['name']

        probability = str(round(item[1]['confidence'] * 100,2))

        name = name + " (" + probability + ")"

        img = cv2.rectangle(img, (x1,y1), (x2,y2), (0, 255, 0), 1)
        cv2.putText(img,name,(x1,y1-10) ,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0, 255, 0))
 
    cv2.imshow("muon_live",img)
    #cv2.resizeWindow("muon_live", 700, 500)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 
 