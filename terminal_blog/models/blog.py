import uuid
import datetime
from models.post import Post
from models.database import Database


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author)

        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_last(collection='posts')

        return cls(author=blog_data[0]['author'],
                   title=blog_data[0]['title'],
                   description='some description',
                   id=blog_data[0]['id'])

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='posts', query={'id': id})
        print(blog_data['title'])

        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description= 'some description',
                   id=blog_data['id'])
