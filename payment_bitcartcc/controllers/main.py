import logging
import pprint

import requests
from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request
from werkzeug import urls
from werkzeug.exceptions import Forbidden

_logger = logging.getLogger(__name__)


class BitcartController(http.Controller):
    _return_url = "/payment/bitcartcc/return/"
    _webhook_url = "/payment/bitcartcc/webhook/"

    @http.route(
        _return_url,
        type="http",
        auth="public",
        methods=["GET", "POST"],
        csrf=False,
        save_session=False,
    )
    def bitcartcc_return_from_checkout(self):
        return request.redirect("/payment/status")

    @http.route(
        _webhook_url, type="http", auth="public", methods=["GET", "POST"], csrf=False
    )
    def bitcart_webhook(self):
        data = request.get_json_data()
        _logger.info(
            "notification received from BitcartCC with data:\n%s", pprint.pformat(data)
        )
        try:
            tx_sudo = request.env["payment.transaction"].sudo()
            provider = tx_sudo.provider_id.search([("code", "=", "bitcartcc")])
            api_url = provider.api_url
            response = requests.get(urls.url_join(api_url, f"/invoices/{data['id']}"))
            response.raise_for_status()
            full_invoice = response.json()
            if (
                full_invoice["status"] != "complete"
                or full_invoice["status"] != data["status"]
            ):
                raise Forbidden()
            tx_sudo._handle_notification_data("bitcartcc", full_invoice)
        except (
            ValidationError,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
        ):  # Acknowledge the notification to avoid getting spammed
            _logger.exception(
                "unable to handle the notification data; skipping to acknowledge"
            )
        return ""
