from django.contrib import admin

# Register your models here.
from .models import Mood
admin.site.register(Mood)

from .models import Comments
admin.site.register(Comments)
