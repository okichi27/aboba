import cv2
import pytesseract

def recognize_digits(image_path):
    # Завантаження зображення
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Видалення шуму та збільшення контрастності
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)

    # Знаходження контурів на зображенні
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ігноруємо занадто маленькі контури
        if cv2.contourArea(contour) < 100:
            continue

        # Виділення контуру з цифрою на зображенні
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Використання Tesseract OCR для розпізнавання цифри
        cropped_digit = gray[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped_digit, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

        # Додавання надпису над виділеною цифрою
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Показати оригінальне зображення з виділеними цифрами
    cv2.imshow('Recognized Digits', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = '/home/rodion/yuliia0/aboba/test/5.jpg'
recognize_digits(image_path)