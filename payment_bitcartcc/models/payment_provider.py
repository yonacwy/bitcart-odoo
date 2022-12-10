from odoo import fields, models


class PaymentProvider(models.Model):
    _inherit = "payment.provider"

    code = fields.Selection(
        selection_add=[("bitcartcc", "BitcartCC")],
        ondelete={"bitcartcc": "set default"},
    )
    api_url = fields.Char(
        string="API URL",
        help="Merchants API URL",
        required_if_provider="bitcartcc",
    )
    admin_url = fields.Char(
        string="Admin URL",
        help="Admin panel URL",
        required_if_provider="bitcartcc",
    )
    store_id = fields.Char(
        string="Store ID",
        help="Store ID",
        required_if_provider="bitcartcc",
    )
