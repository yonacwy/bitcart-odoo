from odoo.addons.payment import reset_payment_provider, setup_provider

from . import controllers, models  # noqa: F401


def post_init_hook(cr, registry):
    setup_provider(cr, registry, "bitcart")


def uninstall_hook(cr, registry):
    reset_payment_provider(cr, registry, "bitcart")
