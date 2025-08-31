# myapp/admin.py
from django.contrib import admin
from .models import Question, Choice, ChoiceCategory, QuestionParagraph, Answer, AnswerChoice
from .models import Product # Import the Product model

admin.site.register(Question)
admin.site.register(ChoiceCategory)
admin.site.register(Choice)
admin.site.register(QuestionParagraph)
admin.site.register(Answer)
admin.site.register(AnswerChoice)

#Admin page にProductモデルを登録
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category']
    #'category' フィールドをラジオボタンとして表示
    radio_fields = {"category": admin.HORIZONTAL}
    