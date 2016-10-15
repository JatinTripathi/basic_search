import os, sys, django, json
from settings import BASE_DIR

sys.path.append(BASE_DIR)
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()

from engine.models import Tag, Image, TagImageScore
from clarifai.rest import ClarifaiApp


file = open('./url.txt')
def readFile():
    nextUrl = file.readline()[:-1]
    nextUrl = nextUrl.strip()

    app = ClarifaiApp()
    model = app.models.get('general-v1.3')

    tags =  model.predict_by_url(nextUrl)
    tags = json.loads(tags)
    for output in tags.output[0].data.concept:
        score = output.value
        tag = output.name
        
    readFile()
readFile()