import cv2 as cv
from JSONParser import parse
from gpt import askGPT
from ocr import extractText
from db import userID, add_user, add_receipt, get_receipts_for_user


receipt = 'resources/Photos/Joe.png'

# get the text from the image
ocr_text = extractText(receipt)

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


    '''
    JSON format:
        {{
        "Shop": <Name of Store/Shop>
        "items": [
            {{"item": "<Item Name>", "price": <Price>}},
            ...
        ],
        "total": <Total Amount>,
        "date": "<Purchase Date>"
    }}
    '''
    user_id = userID("pathav4@mcmaster.ca")
    if (user_id==None):
        try:
            user_id = add_user("varun", "pathav4@mcmaster.ca", "varun123")
        except Exception as e:
            print(f"Error:{e}")
    
    add_receipt(user_id, json["Shop"], json["date"], json["total"], json["items"])


except:
    print("Error parsing JSON ... GPT response may be incorrect")


cv.imshow('receipt', cv.imread(receipt))
cv.waitKey(0)
cv.destroyAllWindows()

    
