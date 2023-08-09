from django.contrib.auth.views import LoginView
from django.contrib.auth.views import (
    LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import path

from users.views import (HomeView, UserRegisterView, UploadUserDataView, UserUploadedBarChartView,
                         UserUploadedPieChartView, UserUpdateView)

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name="user-login"),
    path('register/', UserRegisterView.as_view(), name="user-register"),
    path('logout/', LogoutView.as_view(), name="user-logout"),
    path('update/', UserUpdateView.as_view(), name="user-update"),
    path('file_upload/', UploadUserDataView.as_view(), name="upload-data"),
    path("bar_chart/<int:pk>", UserUploadedBarChartView.as_view(), name="view-bar-chart"),
    path("pie_chart/<int:pk>", UserUploadedPieChartView.as_view(), name="view-pie-chart"),
    path('password_change/',
         PasswordChangeView.as_view(template_name='users/password_change.html', success_url='done/'),
         name='change-password'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name="password_change_done"),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
