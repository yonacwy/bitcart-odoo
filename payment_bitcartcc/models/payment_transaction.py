import logging

import requests
from odoo import models
from odoo.exceptions import ValidationError
from werkzeug import urls

from ..controllers.main import BitcartController

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = "payment.transaction"

    def _get_specific_rendering_values(self, processing_values):
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != "bitcartcc":
            return res
        base_url = self.provider_id.get_base_url()
        data = requests.post(
            urls.url_join(self.provider_id.api_url, "/invoices"),
            json={
                "price": processing_values["amount"],
                "currency": self.currency_id.name,
                "store_id": self.provider_id.store_id,
                "buyer_email": self.partner_email,
                "order_id": processing_values["reference"],
                "notification_url": urls.url_join(
                    base_url, BitcartController._webhook_url
                ),
                "redirect_url": urls.url_join(base_url, BitcartController._return_url),
            },
        ).json()
        return {
            "id": data["id"],
            "checkout_url": urls.url_join(
                self.provider_id.admin_url, f"/i/{data['id']}"
            ),
        }

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        """Override of payment to find the transaction based on BitcartCC data.

        :param str provider_code: The code of the provider that handled the transaction
        :param dict notification_data: The notification data sent by the provider
        :return: The transaction if found
        :rtype: recordset of `payment.transaction`
        :raise: ValidationError if the data match no transaction
        """
        tx = super()._get_tx_from_notification_data(provider_code, notification_data)
        if provider_code != "bitcartcc" or len(tx) == 1:
            return tx

        reference = notification_data.get("order_id")
        tx = self.search(
            [("reference", "=", reference), ("provider_code", "=", "bitcartcc")]
        )
        if not tx:
            raise ValidationError(
                f"BitcartCC: No transaction found matching reference {reference}."
            )
        return tx

    def _process_notification_data(self, notification_data):
        super()._process_notification_data(notification_data)
        if self.provider_code != "bitcartcc":
            return

        txn_id = notification_data.get("id")
        if not txn_id:
            raise ValidationError(f"BitcartCC: Missing value for txn_id ({txn_id}).")
        self.provider_reference = txn_id

        payment_status = notification_data.get("status")
        if payment_status == "complete":
            self._set_done()
        else:
            _logger.info(
                "received data with invalid payment status (%s) for transaction with reference %s",
                payment_status,
                self.reference,
            )
            self._set_error(
                f"BitcartCC: Received data with invalid payment status: {payment_status}"
            )
