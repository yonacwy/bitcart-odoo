{
    "name": "BitcartCC Payments",
    "version": "1.0",
    "author": "BitcartCC",
    "category": "Accounting/Payment Providers",
    "summary": "Self-hosted, open-source cryptocurrency payment processor and developer solutions",
    "website": "https://bitcartcc.com",
    "depends": ["payment"],
    "data": [
        "views/payment_bitcartcc_templates.xml",
        "views/payment_provider_views.xml",
        "views/payment_transaction_views.xml",
        "data/payment_provider_data.xml",
    ],
    "application": True,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "license": "LGPL-3",
}
