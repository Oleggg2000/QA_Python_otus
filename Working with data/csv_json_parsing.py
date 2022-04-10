import json
import csv


with open("user.json", "r") as f:
    users = json.load(f)
    # print(len(users), 212-7*28)

with open("books.csv", "r") as f:
    books = csv.reader(f, delimiter=",")
    next(books)
    i = 0
    collection = []
    for user in users:
        dict_ = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": []
        }
        if i < 15:
            n = 8
        else:
            n = 7
        for _ in range(n):
            book = next(books)
            dict_["books"].append({
                "title": book[0],
                "author": book[1],
                "pages": book[3],
                "genre": book[2]
            })
        collection.append(dict_)
        i += 1

with open("result.json", "w") as f:
    json.dump(collection, f, indent=4)
