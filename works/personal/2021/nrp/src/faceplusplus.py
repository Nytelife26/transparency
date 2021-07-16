from analyze import BaseService
import requests
from io import BufferedReader
import base64

endpoint = "https://api-us.faceplusplus.com/facepp/v3/detect"


class FacePlusPlus(BaseService):
    name = "face++"

    def __init__(self, api_key, api_secret):
        self.key = api_key
        self.secret = api_secret

    def sdk(self, file: BufferedReader) -> dict:
        detected = requests.post(endpoint, params={
            "api_key": self.key,
            "api_secret": self.secret,
            "return_attributes": "age,gender"
        }, files={"image_file": file}).json()
        try:
            detected = detected["faces"][0]["attributes"]
            return {"age": detected["age"]["value"], "gender": detected["gender"]["value"][0].lower()}
        except:
            print("ANALYSIS FAILED!")
            print(detected)
            return {"age": 0, "gender": "N"}
