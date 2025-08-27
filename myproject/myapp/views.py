from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Answer, AnswerChoice

def index(request):
    """
    質問の一覧ページを表示するビュー。
    最新の質問を5つ取得し、テンプレートに渡します。
    """
    # pub_dateの降順で最新の5件の質問を取得
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "myapp/index.html", context)


def detail(request, question_id):
    """
    特定の質問の詳細ページを表示するビュー。
    URLから渡されたquestion_idに基づいて質問を取得します。
    """
    # 存在しないquestion_idが指定された場合は404エラーを返す
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "myapp/detail.html", {"question": question})


def submit_answer(request, question_id):
    """
    詳細ページから送信された回答を処理し、データベースに保存するビュー。
    POSTリクエストのみを受け付けます。
    """
    question = get_object_or_404(Question, pk=question_id)

    # 既存の回答があれば削除
    # if request.user.is_authenticated:
    #     Answer.objects.filter(question=question, user=request.user).delete()

    # Answerモデルに回答を保存
    # answer_textはテキストエリアから取得
    answer = Answer(question=question, answer_text=request.POST.get('text_area_answer', ''))
    answer.save()

    # ラジオボタンの回答を処理
    selected_radio_choice_id = request.POST.get('radio_choice')
    if selected_radio_choice_id:
        choice = get_object_or_404(Choice, pk=selected_radio_choice_id)
        AnswerChoice.objects.create(answer=answer, choice=choice)

    # チェックボックスの回答を処理
    # getlist()を使って複数の選択肢を取得
    selected_checkbox_choices_ids = request.POST.getlist('checkbox_choices')
    for choice_id in selected_checkbox_choices_ids:
        choice = get_object_or_404(Choice, pk=choice_id)
        AnswerChoice.objects.create(answer=answer, choice=choice)
        
    # セレクトオプションの回答を処理
    selected_select_option_id = request.POST.get('select_option')
    if selected_select_option_id:
        choice = get_object_or_404(Choice, pk=selected_select_option_id)
        AnswerChoice.objects.create(answer=answer, choice=choice)

    # 回答処理後、同じ質問の詳細ページにリダイレクト
    return HttpResponseRedirect(reverse("myapp:detail", args=(question.id,)))
