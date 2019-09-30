import unittest
from app.models import Blog,Writer
from flask_login import current_user
from app import db


class TestBlog(unittest.TestCase):

    def setUp(self):
        self.writer_stacy=Writer(username='stacy',password='123',email='stacy@gmail.com')
        self.new_post= Blog(title='the old woman',content='hello',author='stacy')    


    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Blog))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.content,'hello')
        self.assertEquals(self.new_post.title,'the old woman')  

    def test_save_blog(self):
        self.new_post.save_blog()  

    def test_get_blogs(self):
        self.new_post.save_blog()
        blog_posts = Blog.get_blogs(123)
             
        