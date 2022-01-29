import requests

image = {'image': open('data/test_photo.jpeg', 'rb').read()}

r1 = requests.get("http://0.0.0.0:5000/")
print(r1.text)

r2 = requests.post("http://localhost:5000/get_prob", files=image)
print(r2.text) # "Male" or "Female"