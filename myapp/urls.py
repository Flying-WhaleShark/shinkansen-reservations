# myapp/urls.py

from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    # 質問一覧を表示するページ
    path("", views.index, name="index"),
    # 特定の質問の詳細ページを表示するページ
    path("<int:question_id>/", views.detail, name="detail"),
    # 回答を送信するための処理を行うページ
    path("<int:question_id>/submit_answer/", views.submit_answer, name="submit_answer"),
]