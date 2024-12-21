import cv2 as cv
import pytesseract

def processImage(image):

    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #blurred = cv.GaussianBlur(gray, (5,5), 0)

    #cv.imshow('blurred', blurred)
    #cv.waitKey(0)
    return gray

def extractText(processed_img):
    text = pytesseract.image_to_string(processed_img, lang='eng', config='--psm 6')
    return text

if __name__ == "__main__":

    image = 'Photos/Joe.png'
    processed_img = processImage(image)

    cv.imshow('processed', processed_img)
    cv.waitKey(0)

    text = extractText(processed_img)

    print(text)
