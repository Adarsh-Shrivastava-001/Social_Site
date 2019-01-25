from django.contrib import admin
from comments.models import PostComments,QuestionComments

# Register your models here.

admin.site.register(PostComments)
admin.site.register(QuestionComments)