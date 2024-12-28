import cv2 as cv
from JSONParser import parse
from gpt import askGPT
from ocr import extractText


image = 'resources/Photos/Joe.png'

# get the text from the image
ocr_text = extractText(image)

#debugging - OCR Text
o = open("resources/ocr_text.txt", "w")
o.write(ocr_text)
o.close()

# get the ocr text formatted with gpt - return a json for later db upload
formatted = askGPT(ocr_text) 

#debugging - GPT's response
f = open("resources/receiptJSON.txt", "w")
f.write(formatted)
f.close()


try:
    json = parse(formatted) # extract only the json from the response + parse it
    print(json)
except:
    print("Error parsing JSON ... GPT response may be incorrect")


cv.imshow('image', cv.imread(image))
cv.waitKey(0)
cv.destroyAllWindows()

    
