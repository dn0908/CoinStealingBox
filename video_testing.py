from imports import *

cv2.destroyAllWindows()

def preProcessing(img):
    preImg = cv2.GaussianBlur(img, (5, 5), 3)
    thresh1 = 30
    thresh2 = 100
    preImg = cv2.Canny(preImg, thresh1, thresh2)
    kernel = np.ones((3, 3), np.uint8)
    preImg = cv2.dilate(preImg, kernel, iterations=1)
    preImg = cv2.morphologyEx(preImg, cv2.MORPH_CLOSE, kernel)

    return preImg

cam = cv2.VideoCapture(1)

while True:
    _, frame = cam.read()
    hight, width, _ = frame.shape
    print('frame:',hight, '-', width)
    cropframe = frame[150:350, 250:450]

    # 만원
    green_lower=(30,50,50)
    green_higher=(40,255,255)
    green = cv2.inRange(cropframe, green_lower, green_higher)
    cv2.imshow('green',green)
    green_contours, _ = cv2.findContours(green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in green_contours:
        print('GREEN == 10000 WON')

    # 천원
    blue_lower=(80,80,0)
    blue_higher=(200,100,20)
    blue = cv2.inRange(cropframe, blue_lower, blue_higher)
    cv2.imshow('blue',blue)
    blue_contours, _ = cv2.findContours(blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in blue_contours:
        print('BLUE == 1000 WON')

    # 오만원
    yellow_lower=(80,180,80)
    yellow_higher=(100,255,100)
    yello = cv2.inRange(cropframe, yellow_lower, yellow_higher)
    cv2.imshow('yello',yello)
    yello_contours, _ = cv2.findContours(yello, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in yello_contours:
        print('YELLO == 50000 WON')

    
    preImg = preProcessing(cropframe)
    contours, _ = cv2.findContours(preImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        
        cv2.drawContours(preImg,[cnt],0,255,-1)
        # print('contour found')
        
        regions = measure.regionprops(preImg)
        circle = regions[0]
        yc, xc = circle.centroid
        radius = circle.equivalent_diameter / 2.0
        if radius < 55:
            continue
        # print("radius =",radius, "  center =",xc,",",yc)
        print("radius =",radius)
        xx = int(round(xc))
        yy = int(round(yc))
        rr = int(round(radius))
        cv2.circle(cropframe, (xx,yy), rr, (0, 0, 255), 2)
        if 75 < radius < 79:
            print("500 WON")
        elif 68 < radius < 72:
            print("100 WON")
        elif 62 < radius < 66:
            print("50 WON")


    cv2.imshow('Video', cropframe)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break