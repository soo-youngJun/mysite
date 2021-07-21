from django.urls import path
from pybo import views

app_name = 'pybo'
# url 별칭 -> 네임 스페이스

urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # path('answer/modify/<int:question_id>/', views.answer_modify, name='answer_modify'),


    path('jqtest/', views.jqtest, name='jqtest'),
    path('imgtest/', views.imgtest, name='imgtest'),
    path('market/', views.market, name='market'),
    path('components/', views.components, name='components'),
]