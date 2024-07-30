from rest_framework import serializers

from .models import Transaction


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("id", "txn_id", "amount", "type", "parent")
