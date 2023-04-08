from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # previous login url
    #path('login/', views.user_login, name='login')

    # Home page
    path('', views.home, name="home"),
    path('contact', views.contact, name='contact'),

    # Login Urls
    # path('login/', auth_views.LoginView.as_view(), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
     
    # # password change urls.
    # path('password-change/',
    #     auth_views.PasswordChangeView.as_view(),
    #     name='password_change'),
    # path('password_change/done/',
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name='password_change_done'),

    # # Reset password urls
    # path('password-reset/',
    #     auth_views.PasswordResetView.as_view(),
    #     name='password_reset'),
    # path('password-reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'),
    # path('password-reset/complete/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'),

    # New urls
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('quote/', views.quote, name='quote'),
    path('quotes/', views.quotes_list, name='quotes_list'),
]
