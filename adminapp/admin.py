from django.contrib import admin
from .models import *

admin.site.register(Task)

from .models import Feedback

admin.site.register(Feedback)
