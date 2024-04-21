from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # 追記


urlpatterns = [
    path('signup/', views.UserCreateAndLoginView.as_view(
        template_name='accounts/signup.html',
        success_url='/tasks',
        ), name='signup'),    # 変更
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
]