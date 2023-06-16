# for threshold testing...
# from imports import *

# width = 640
# height = 480

# cap = cv2.VideoCapture(1) # for windows | 0 : labtop cam | 1 : webcam
# cap.set(3, width)
# cap.set(4, height)

# totalWon = 0

# myColorFinder = ColorFinder(False)
# # Custom Orange Color -- change
# hsvVals = {'hmin': 0, 'smin': 0, 'vmin': 145, 'hmax': 63, 'smax': 91, 'vmax': 255}
# cv2.destroyAllWindows()

# def empty(a):
#     pass

# cv2.namedWindow("Threshold Settings")
# cv2.resizeWindow("Threshold Settings", 640, 240)
# cv2.createTrackbar("Threshold1", "Threshold Settings", 219, 255, empty)
# cv2.createTrackbar("Threshold2", "Threshold Settings", 233, 255, empty)


# def preProcessing(img):
#     preImg = cv2.GaussianBlur(img, (5, 5), 3)
#     thresh1 = cv2.getTrackbarPos("Threshold1", "Threshold Settings")
#     thresh2 = cv2.getTrackbarPos("Threshold2", "Threshold Settings")
#     preImg = cv2.Canny(preImg, thresh1, thresh2)
#     kernel = np.ones((3, 3), np.uint8)
#     preImg = cv2.dilate(preImg, kernel, iterations=1)
#     preImg = cv2.morphologyEx(preImg, cv2.MORPH_CLOSE, kernel)

#     return preImg


# while True:
#     success, img = cap.read()
#     preImg = preProcessing(img)
#     imgContours, foundCont = cvzone.findContours(img, preImg, minArea=20)

#     totalMoney = 0
#     imgCount = np.zeros((480, 640, 3), np.uint8)

#     if foundCont:
#         for count, contour in enumerate(foundCont):
#             peri = cv2.arcLength(contour['cnt'], True)
#             approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)

#             if len(approx) > 5:
#                 area = contour['area']
#                 x, y, w, h = contour['bbox']
#                 imgCrop = img[y:y + h, x:x + w]
#                 # cv2.imshow(str(count),imgCrop)
#                 imgColor, mask = myColorFinder.update(imgCrop, hsvVals)
#                 whitePixelCount = cv2.countNonZero(mask)
#                 # print(whitePixelCount)

#                 if area < 2050:
#                     totalWon += 5
#                 elif 2050 < area < 2500:
#                     totalWon += 1
#                 else:
#                     totalWon += 2

#     print(totalWon)
#     cvzone.putTextRect(imgCount, f'Rs.{totalWon}', (100, 200),scale=10,offset=30,thickness=7)

#     imgStacked = cvzone.stackImages([img, preImg, imgContours, imgCount], 2, 1)
#     cvzone.putTextRect(imgStacked, f'Rs.{totalWon}', (50, 50))

#     cv2.imshow("Image", imgStacked)

#     if cv2.waitKey(1) & 0xFF == ord('q'): # press q to quit
#         break

# cv2.destroyAllWindows()



#################################################
########## Erased when changed to auto ##########
def get_money_value_index_manual(button):
    if not button.pressed: # This means break in cv2.waitKey part
        print("Type money you want to put")
        money = int(input())
        
    return money