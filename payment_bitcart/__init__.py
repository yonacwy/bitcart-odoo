from odoo.addons.payment import reset_payment_provider, setup_provider

from . import controllers, models  # noqa: F401

    
def post_init_hook(env):
    setup_provider(env, 'bitcart')


def uninstall_hook(env):
    reset_payment_provider(env, 'bitcart')    
