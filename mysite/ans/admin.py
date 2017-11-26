from django.contrib import admin
from .models import Question, Answer, Upvote


admin.site.register([Question, Answer, Upvote])
