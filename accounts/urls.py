from django.urls import path
from accounts.views import account_create, account_list, account_update, account_delete, account_detail, followup_create

app_name = "accounts"

urlpatterns = [
    path('', account_list, name='account-list'),
    path('create/', account_create, name='account-create'),
    path('<int:pk>/update/', account_update, name='account-update'),
    path('<int:pk>/delete/', account_delete, name='account-delete'),
    path('<int:pk>/', account_detail, name='account-detail'),
    path('<int:pk>/followups/create/', followup_create, name='account-followup-create'),
]