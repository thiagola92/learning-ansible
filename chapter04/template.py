from bson import ObjectId

with open('example.txt', 'w') as f:
    f.write(str(ObjectId()))