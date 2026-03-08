# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    receipt_footer_message = fields.Char(
        string='Receipt Footer Message',
        default='Thank you for your business!',
        help='Custom message displayed at the bottom of receipts and WhatsApp messages'
    )
