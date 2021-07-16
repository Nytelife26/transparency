from analyze import BaseService
import boto3
from botocore.config import Config
from io import BufferedReader


class Rekognition(BaseService):
    name = "rekognition"

    def __init__(self, access_key: str, secret_key: str):
        self.client = boto3.client("rekognition",
                                   config=Config(region_name="eu-west-2"),
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key)

    def sdk(self, file: BufferedReader) -> dict:
        detection = self.client.detect_faces(
            Image={"Bytes": file.read()},
            Attributes=["ALL"]
        )
        try:
            detection = detection["FaceDetails"][0]
            return {"age": sum(detection["AgeRange"].values()) // 2,
                    "gender": detection["Gender"]["Value"][0].lower()}
        except:
            print("ANALYSIS FAILED!")
            print(detection)
            return {"age": 0, "gender": "N"}
