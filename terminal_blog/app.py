from models.post import Post
from database import Database

__author__ = 'jcrh'

Database.initialize()

post = Post('Post 1', 'Post1 content', 'Post author')

print(post.content)



## ***** Mongo connection ***********
# from pymongo import MongoClient
# client = MongoClient()

# uri = "mongodb://127.0.0.1:27017"

# db = client['fullstack']
# collection = db.students

# students = collection.find({})
# student_list = []

# students = [student for student in collection.find({})]
# print(students)
# for student in students:
#     print(student)


# %%%%%%%%%%%% OOP %%%%%%%%%
