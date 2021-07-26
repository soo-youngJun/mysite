from django.urls import path
from pybo import views

app_name = 'pybo'
# url 별칭 -> 네임 스페이스

urlpatterns = [
    # 인덱스 메인
    path('', views.index, name='index'),
    # 질문/답변 게시판
    path('board/', views.board, name='board'),
    # 나의 프로필
    path('profile/', views.profile, name='profile'),
    # 상세 페이지
    path('<int:question_id>/', views.detail, name='detail'),
    # 답변 등록
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # 질문 등록
    path('question/create/', views.question_create, name='question_create'),
    # 질문 수정
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # 질문 삭제
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # 답변 수정
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    # 답변 삭제
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    # 질문 추천
    path('vote/question/<int:question_id>/', views.vote_question, name='vote_question'),
    # 질문 댓글 등록
    path('comment/create/question/<int:question_id>', views.comment_create_question, name='comment_create_question'),

    path('jqtest/', views.jqtest, name='jqtest'),
    path('imgtest/', views.imgtest, name='imgtest'),
    path('market/', views.market, name='market'),
    path('components/', views.components, name='components'),
]