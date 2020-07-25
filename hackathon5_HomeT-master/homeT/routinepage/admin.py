from django.contrib import admin
from .models import Routine
from .models import Comment
# Register your models here.

admin.site.register(Routine)
admin.site.register(Comment)