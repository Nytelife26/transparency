from analyze import analyze
from glob import glob
import sys
from az import Azure
from faceplusplus import FacePlusPlus
from rekognition import Rekognition
import json

AZURE_TOKEN = ""
AZURE_ENDPOINT = ""
FACEPP_KEY = ""
FACEPP_SECRET = ""
REKOG_KEY = ""
REKOG_SECRET = ""

services = [Azure(AZURE_TOKEN, AZURE_ENDPOINT),
            FacePlusPlus(FACEPP_KEY, FACEPP_SECRET),
            Rekognition(REKOG_KEY, REKOG_SECRET)]

analyze(services, glob(sys.argv[1]), wait=3)
