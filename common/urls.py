from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
# 제네릭 뷰 방식 - 함수를 직접 정의할 필요가 없음(기본적으로 로그인, 로그아웃 클래스가 있음)