import uuid
from django.db import models


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    txn_id = models.PositiveBigIntegerField(unique=True, db_index=True)
    amount = models.PositiveIntegerField()
    type = models.CharField(max_length=15)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE, null=True, blank=True, related_name="children",
                               to_field="txn_id")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.txn_id)


