import requests
import json

BASE_URL = "https://m9ggmj-5000.csb.app/"
headers = {'Content-Type': 'application/json'}


data= [
    { "title": "To Kill a Mockingbird", "author": "Harper Lee" },
    { "title": "1984", "author":"George Orwell" },
    { "title": "The Great Gatsby", "author": "F. Scott Fitzgerald" }
]

for i in range(len(data)):
    response = requests.post(BASE_URL + f"books/{str(i + 1)}", data=json.dumps(data[i]), headers=headers)
    print(response.json())

input()


# getAllBooks
# response = requests.get(BASE_URL + "books")
# print(response.json())
# input()

# # getBook
# response = requests.get(BASE_URL + "books/1")
# print(response.json())
# input()

# Create Book
# data = { "title": "Pride and Prejudice", "author":"Jane Austen" }
# response = requests.post(BASE_URL + "books/1", data=json.dumps(data), headers=headers)
# print(response.json())
# input()

# # Update whole book
# data = { "title": "The Catcher in the Rye", "author":"J.D. Salinger" }
# response = requests.put(BASE_URL + "books/1", data=json.dumps(data), headers=headers)
# print(response.json())
# input()

# Delete Book
# response = requests.delete(BASE_URL + "books/2")
# print(response.json())
# input()


# Delete all books
# response = requests.delete(BASE_URL + "books/clear")
# print(response.json())
# input()
