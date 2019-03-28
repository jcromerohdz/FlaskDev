from models.database import Database
from models.blog import Blog

class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('posts', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter a title: ")
        description = input("Enter a blog description: ")
        blog = Blog(author=self.user, title=title, description=description)

        blog.save_to_mongo()
        self.user_blog=blog

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='posts', query={})
        for b in blogs:
            print("ID: {}, Title: {}, Author: {}".format(b['id'], b['title'], b['author']))

    def _view_blog(self):
        blog_to_read = input("Enter the ID of the blog you'd like to read (copy and pasete from the list): ")
        blog = Database.find_one('posts', {'id':blog_to_read})
        print("DATE: {}, Title: {}\n\n{}".format(blog['created_date'], blog['title'], blog['content']))
