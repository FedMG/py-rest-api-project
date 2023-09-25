import requests

BASE_URL = "https://zvq558-5000.csb.app/"

# data= [
#     { "likes": 10, "views": 1000, "name": "The best video of the world!" },
#     { "likes": 30, "views": 10000, "name": "Cat videos!" },
#     { "likes": 400, "views": 15500, "name": "Cooking a cake" }
# ]

# for i in range(len(data)):
#     response = requests.post(BASE_URL + f"video/{str(i)}", data[i])
#     print(response.json())

# input()

# response = requests.delete(BASE_URL + "video/0")
# print(response)
# input()


response = requests.patch(BASE_URL + "video/2", {})
print(response.json())
input()

# response = requests.get(BASE_URL + "video/2")
# print(response.json())

# response = requests.get(BASE_URL + "helloWorld/tim/19")
# print(response.json())

# response = requests.post(BASE_URL + "helloWorld")
# print(response.json())

