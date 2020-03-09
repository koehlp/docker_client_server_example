import requests

url = "http://172.17.0.2:8888/videoframe"
#url = "http://localhost:8888/videoframe"
files = {'videoframe': open('image_185540_3.jpg', 'rb'), 'framename' : "image_185540_3.jpg"}
resp = requests.post(url, files=files)


print(resp.content)