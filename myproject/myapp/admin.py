# myapp/admin.py
from django.contrib import admin
from .models import Question, Choice, ChoiceCategory, QuestionParagraph, Answer, AnswerChoice

admin.site.register(Question)
admin.site.register(ChoiceCategory)
admin.site.register(Choice)
admin.site.register(QuestionParagraph)
admin.site.register(Answer)
admin.site.register(AnswerChoice)
