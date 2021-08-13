from imagesite.settings import AWS_ACCESS_KEY, AWS_SECRET_KEY
import boto3
import botocore
import os
import urllib
import uuid

#returns image name
def downloadImageFromURL(url):
    imgPath = 'utils/swap/{}.jpg'.format(uuid.uuid1())
    urllib.request.urlretrieve(url, imgPath)
    return imgPath

#returns s3 image link
def uploadImageToS3(img):
    session = boto3.Session(
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_KEY,
    )
    s3 = session.resource('s3')

    #prepare image for bucket upload
    bucketName = "image-api-hackathon"
    data = open(img, 'rb')
    imgFile = '{}.jpg'.format(uuid.uuid1())

    s3.Bucket(bucketName).put_object(Key=imgFile, Body=data, ContentType='image/jpg')

    #delete file from swap
    try: os.remove(img)
    except: pass

    url = "https://" + bucketName + ".s3.amazonaws.com/" + imgFile
    return url





