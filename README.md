# Bitcart plugin for Odoo

## Integration Requirements

This version requires the following:

* Your Odoo instance
* Running Bitcart instance: [deployment guide](https://docs.bitcart.ai/deployment)

## Installing the Plugin

1. Install the plugin via [App store](https://apps.odoo.com/apps/modules/16.0/payment_bitcart) or add `payment_bitcart` directory to your addons directory (You can take [the latest release](https://github.com/bitcart/bitcart-odoo/releases/latest), unzip it and get `payment_bitcart` from there)

2. From your Odoo apps page, activate "Bitcart Payments" app

3. Configure the plugin (see details below)

## Plugin Configuration

After you have enabled the Bitcart plugin, the configuration steps are:

1. Enter your admin panel URL (for example, https://admin.bitcart.ai) without slashes. If deployed via configurator, you should use https://bitcart.yourdomain.com/admin
2. Enter your merchants API URL (for example, https://api.bitcart.ai) without slashes. If deployed via configurator, you should use https://bitcart.yourdomain.com/api
3. Enter your store ID (click on id field in Bitcart's admin panel to copy id)

Enjoy!
