from analyze import BaseService
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from io import BufferedReader


class Azure(BaseService):
    name = "azure"

    def __init__(self, token, endpoint):
        self.client = FaceClient(endpoint, CognitiveServicesCredentials(token))

    def sdk(self, file: BufferedReader) -> dict:
        detected = self.client.face.detect_with_stream(
            file, return_face_attributes=["age", "gender"])
        try:
            detected = detected[0].face_attributes
            return {"age": int(detected.age), "gender": detected.gender.value[0]}
        except:
            print("ANALYSIS FAILED!")
            print(detected)
            return {"age": 0, "gender": "N"}
