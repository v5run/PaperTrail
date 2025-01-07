from beta.JSONParser import parse
from beta.gpt import askGPT
from beta.ocr import extractText
from beta.db import userID, add_receipt
from beta.s3_upload import upload_to_s3

class Receipt:

    def __init__(self, receipt_image):
        self.receipt = receipt_image

    def upload(self):
        #add receipt to s3
        upload_to_s3(self.receipt)

        self.ocr_text = extractText(self.receipt)
        self.formatted = askGPT(self.ocr_text)
        self.json = self.parseJSON(self.formatted)

        self.user_id = userID("pathav4@mcmaster.ca")

        # add the receipt to postgresql database
        add_receipt(self.user_id, self.json["Shop"], self.json["date"], self.json["total"], self.json["items"])

    def parseJSON(self, formatted):
        try:
            json = parse(formatted)
            return json
        except:
            print("Error parsing JSON ... GPT response may be incorrect")
            return None