
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title']


from .models import AddCourse

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']

from .models import Marks
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']