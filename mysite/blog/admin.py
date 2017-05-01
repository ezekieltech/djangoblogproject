#Here, we are importing the admin, the Post model, and then we're registering the Post model.
from django.contrib import admin

# Register your models here.
#from django.contrib import admin
from blog.models import Post
admin.site.register(Post)
