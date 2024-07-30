from django.urls import path

from .views import CreateGetTransactionView, GetTransactionListView

urlpatterns = [
    path("transaction/<int:txn_id>/", CreateGetTransactionView.as_view()),
    path("types/<slug:txn_type>/", GetTransactionListView.as_view()),
]
