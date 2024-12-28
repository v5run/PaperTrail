import cv2 as cv
import pytesseract

def extractText(image):

    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #ocr extraction
    text = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')
    return text
