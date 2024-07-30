from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from .models import Transaction


class CreateGetTransactionView(APIView):

    def get(self, request, *args, **kwargs):
        txn_id = kwargs.get("txn_id")
        try:
            txn = Transaction.objects.get(txn_id=txn_id)
        except ObjectDoesNotExist as e:
            return Response({"error": "Transaction Does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        resp = {
            "amount": txn.amount,
            "type": txn.type,
        }
        if txn.parent:
            resp["parent_id"] = txn.parent.txn_id

        return Response(resp, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        txn_id = kwargs.get("txn_id")
        data = request.data

        parent = None
        if data.get("parent_id"):
            try:
                parent = Transaction.objects.get(txn_id=data.get("parent_id"), is_active=True, is_deleted=False)
            except ObjectDoesNotExist as e:
                return Response({"error": "parent_id Does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        txn = Transaction(
            txn_id=txn_id,
            amount=data.get("amount"),
            type=data.get("type"),
            parent=parent
        )

        try:
            txn.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"status": "ok"}, status=status.HTTP_201_CREATED)


class GetTransactionListView(APIView):
    def get(self, request, *args, **kwargs):
        txn_type = kwargs.get("txn_type")
        transactions = Transaction.objects.filter(type=txn_type).values_list("amount", flat=True)

        return Response(transactions, status=status.HTTP_200_OK)
