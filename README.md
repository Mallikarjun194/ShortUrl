# ShortUrl
Generates a shorturl for given url.

Steps:

1. Build the docker image using dockerfile.
2. Run the container using: 
   docker run -p <localport>:5000 <image-name>
   
3. The following are the API EndPoints.
   
    1) GET API:
       http://127.0.0.1:8000/get?url=www.Google.com
       Sample-output: {"www.Google.com": "myapp.com/Ti4d2"}
       key will be original url and value will be shortened url.
       
    2) POST API:
       http://127.0.0.1:8000/create
       Payload: {"url": "www.Amazon.com"}
       Sample-output: {"Success": "Your short url is myapp.com/zF4j5"}
       
    3) PUT API:
       http://127.0.0.1:8000/update
       Payload: {"url": "www.Amazon.com"}
       Sample-output: {"Success": "Your updated short url is myapp.com/FEfDI"}
   
    4) DELETE API:
       http://127.0.0.1:8000/delete
       Payload: {"url": "www.Amazon.com"}
       {"Success:": "url deleted successfully www.Amazon.com"}
