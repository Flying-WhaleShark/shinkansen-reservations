# reservation/views.py

from django.shortcuts import render

# メインメニューページ
def index(request):
    return render(request, 'reservation/index.html')

# 新規予約ページ
def book(request):
    # 予約フォームの処理ロジックをここに書く
    return render(request, 'reservation/book.html')

# 予約確認ページ
def check(request):
    # 予約確認のロジックをここに書く
    return render(request, 'reservation/check.html')

# 予約キャンセルページ
def cancel(request):
    # 予約キャンセルのロジックをここに書く
    return render(request, 'reservation/cancel.html')

# マイページ
def mypage(request):
    # ユーザー情報や予約履歴の表示ロジックをここに書く
    return render(request, 'reservation/mypage.html')
