import cv2
import imutils
import pytesseract

original_image = cv2.imread('/home/rodion/yuliia0/aboba/tasks/task8/numer_car/car_numer2.jpg')
original_image = imutils.resize(original_image, width=500 )
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) 
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)


contours, new = cv2.findContours(gray_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]

# stores the license plate contour
screenCnt = None

# draws top 30 contours
cv2.drawContours(original_image, contours, -1, (0, 255, 0), 3)
cv2.imshow("img2", original_image)

count = 0
idx = 7

for c in contours:
    # approximate the license plate contour
    contour_perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * contour_perimeter, True)

    # Look for contours with 4 corners
    if len(approx) == 4:
        screenCnt = approx

        # find the coordinates of the license plate contour
        x, y, w, h = cv2.boundingRect(c)
        new_img = original_image [ y: y + h, x: x + w]

        # stores the new image
        cv2.imwrite('./'+str(idx)+'.png',new_img)
        idx += 1
        break

# draws the license plate contour on original image
cv2.drawContours(original_image , [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("detected license plate", original_image )


# converts the license plate characters to string
text = pytesseract.image_to_string(original_image, lang='eng') 

print("License plate is:", text)
cv2.waitKey(0)
cv2.destroyAllWindows()