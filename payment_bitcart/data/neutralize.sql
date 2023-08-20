-- disable bitcart payment provider
UPDATE payment_provider
   SET api_url = NULL,
       admin_url = NULL,
       store_id = NULL;
