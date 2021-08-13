# image-api

## Getting Started
1. Install Python dependencies with `pip3 install -r requirements.txt` 
2. Start the server with  `python3 manage.py runserver`
3. The imagesite Django Server should be running on your `localhost`

>Note: AWS Credentials need to be added to `imagesite/settings.py`

## Endpoints
> **URL for API:** `v1/`

`grayscale/`
   - HTTP METHOD: `GET`
   - PARAMS
     - img: url of web image
