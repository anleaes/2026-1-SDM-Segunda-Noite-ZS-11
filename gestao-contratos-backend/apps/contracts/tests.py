from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase

from .models import Contract
from .serializer import ContractSerializer


class ContractTotalTests(SimpleTestCase):
    def test_total_value_is_read_only_in_api(self):
        self.assertTrue(ContractSerializer().fields['total_value'].read_only)

    @patch('contracts.models.Contract.objects.filter')
    def test_recalculate_total_value_uses_item_sum(self, filter_contract):
        contract = MagicMock(spec=Contract)
        contract.pk = 10
        contract.items = MagicMock()
        contract.items.aggregate.return_value = {'total': 350}

        total = Contract.recalculate_total_value(contract)

        self.assertEqual(total, 350)
        filter_contract.assert_called_once_with(pk=10)
        filter_contract.return_value.update.assert_called_once_with(total_value=350)
