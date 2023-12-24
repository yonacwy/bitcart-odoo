# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo import http
from odoo.http import request
from datetime import datetime
import calendar, math, re, io, base64, os, json, werkzeug
import logging
_logger = logging.getLogger(__name__)


class BitcartMain(models.Model):
    _name = "bitcart.main"
    _description = "Bitcart Main"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True)


