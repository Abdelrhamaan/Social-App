from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


# app_name = 'account'
urlpatterns = [ 
    # path('login/', views.user_login, name = 'login')
    # -------login / logout by django authentication--------
    #     path('login/', auth_views.LoginView.as_view(), name='login'),
    #     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #     path('password-change/', auth_views.PasswordChangeView.as_view(),
    #          name='password_change'),
    #     path('password-change_done/', auth_views.PasswordChangeDoneView.as_view(),
    #          name='password_change_done'),
    #     path('password-reset/', auth_views.PasswordResetView.as_view(),
    #          name='password_reset'),
    #     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
    #          name='password_reset_done'),
    #     path('password-reset/<uidb64>/<token>/',
    #          auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #     path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
    #          name='password_reset_complete'),
    #   ------ use django urls instead of above urls ------
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('', views.dashboard, name='dashboard'),
    path('users/', views.user_list, name='user_list'),
    # path('users/follow/', views.user_follow, name='user_follow'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>', views.user_detail, name='user_detail'),
]
