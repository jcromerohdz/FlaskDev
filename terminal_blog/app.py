from models.post import Post
from models.database import Database

__author__ = 'jcrh'

Database.initialize()


# Insert to mongo
# post = Post(blog_id='12345',
#             title='Super post',
#             content='This the content we send by the app',
#             author='Christian')


#post.save_to_mongo()



# Read from mongo
# post = Post.from_mongo('8111280e864f47229d189b312ad6d643')
#
# print(post)

# posts = Post.from_blog('12345')
# for post in posts:
#     print(post)



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
