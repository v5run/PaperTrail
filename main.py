import cv2 as cv
import pytesseract
from gpt4all import GPT4All

model_path = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
gpt = GPT4All(model_path)

def processImage(image):

    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    return gray

def extractText(processed_img):
    text = pytesseract.image_to_string(processed_img, lang='eng', config='--psm 6')
    return text

def parseText(text):
    prompt = f"""
    You are a helpful assistant. Please extract the following details from the receipt text:
    1. List of items with their prices.
    2. Total amount.
    3. Purchase date.

    Here is the receipt text:
    {text}

    Provide the output in this JSON format:
    {{
        "Shop": <Name of Store/Shop>
        "items": [
            {{"item": "<Item Name>", "price": <Price>}},
            ...
        ],
        "total": <Total Amount>,
        "date": "<Purchase Date>"
    }}
    """

    response = gpt.generate(prompt)
    return response


if __name__ == "__main__":

    image = 'resources/Photos/repair_shop.png'
    processed_img = processImage(image)

    text = extractText(processed_img)
    o = open("resources/ocr_text.txt", "w")
    o.write(parseText(text))
    o.close()

    f = open("resources/receiptJSON.txt", "w")
    f.write(parseText(text))
    f.close()

    cv.imshow('processed', processed_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    
