from decimal import Decimal
from unittest.mock import MagicMock, patch

from django.db import models
from django.test import SimpleTestCase

from contracts.models import Contract
from services.models import Service

from .models import ContractItem
from .serializer import ContractItemSerializer


class ContractItemTotalTests(SimpleTestCase):
    def test_total_price_is_read_only_in_api(self):
        self.assertTrue(ContractItemSerializer().fields['total_price'].read_only)

    @patch.object(models.Model, 'save')
    def test_save_calculates_item_total_and_updates_contract(self, model_save):
        contract = Contract(id=10)
        contract.recalculate_total_value = MagicMock()
        item = ContractItem(
            quantity=3,
            unitary_price=Decimal('25.50'),
            contract=contract,
            service=Service(id=5),
            description='Item de teste',
        )

        item.save()

        self.assertEqual(item.total_price, Decimal('76.50'))
        model_save.assert_called_once()
        contract.recalculate_total_value.assert_called_once()
