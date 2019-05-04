from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','que_type','question_text']
    fields =['pub_date','question_text']
class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text','votes']
# admin.site.register(Question,QuestionAdmin)