from django.urls import path

from .views import CreateGetTransactionView

urlpatterns = [
    path("transaction/<int:txn_id>/", CreateGetTransactionView.as_view()),
]
