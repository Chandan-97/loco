from django.urls import path

from .views import CreateTransactionView

urlpatterns = [
    path("transaction/<int:txn_id>/", CreateTransactionView.as_view()),
]
