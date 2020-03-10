from django.contrib import admin
from import_export import resources

from .models import Question
from .models import Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

class QuestionResource(resources.ModelResource):
  class Meta:
    model = Question