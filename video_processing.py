from imports import *

def preProcessing(img):
    preImg = cv2.GaussianBlur(img, (5, 5), 3)
    thresh1 = 30
    thresh2 = 100
    preImg = cv2.Canny(preImg, thresh1, thresh2)
    kernel = np.ones((3, 3), np.uint8)
    preImg = cv2.dilate(preImg, kernel, iterations=1)
    preImg = cv2.morphologyEx(preImg, cv2.MORPH_CLOSE, kernel)

    return preImg


def ohmanwon(img):
    yellow_lower=(80,180,80)
    yellow_higher=(100,255,100)
    yellow = cv2.inRange(img, yellow_lower, yellow_higher)
    # cv2.imshow('yellow',yellow)
    yellow_contours, _ = cv2.findContours(yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in yellow_contours:
        print('YELLOW == 50000 WON')
        moneyvalue = 50000
        return moneyvalue

def manwon(img):
    green_lower=(30,50,50)
    green_higher=(40,255,255)
    green = cv2.inRange(img, green_lower, green_higher)
    # cv2.imshow('green',green)
    green_contours, _ = cv2.findContours(green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in green_contours:
        print('GREEN == 10000 WON')
        moneyvalue = 10000
        return moneyvalue

def ohcheonwon(img):
    red_lower=(100,100,220)
    red_higher=(150,150,220)
    red = cv2.inRange(img, red_lower, red_higher)
    # cv2.imshow('red',red)
    red_contours, _ = cv2.findContours(red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in red_contours:
        print('RED == 5000 WON')
        moneyvalue = 5000
        return moneyvalue

def cheonwon(img):
    blue_lower=(80,80,0)
    blue_higher=(200,100,20)
    blue = cv2.inRange(img, blue_lower, blue_higher)
    # cv2.imshow('blue',blue)
    blue_contours, _ = cv2.findContours(blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in blue_contours:
        print('BLUE == 1000 WON')
        moneyvalue = 1000
        return moneyvalue


def coin(img):
    preImg = preProcessing(img)
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
        cv2.circle(img, (xx,yy), rr, (0, 0, 255), 2)
        if 75 < radius < 79:
            print("500 WON Detected")
            moneyvalue = 500
            return moneyvalue
        elif 68 < radius < 72:
            print("100 WON Detected")
            moneyvalue = 100
            return moneyvalue
        elif 62 < radius < 66:
            print("50 WON Detected")
            moneyvalue = 50
            return moneyvalue
