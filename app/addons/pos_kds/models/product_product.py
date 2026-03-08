import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    prepair_time_minutes = fields.Float(
        string='Preparation Time (minutes)',
        digits=(12, 2),
        help="Enter preparation time in minutes (e.g., 5.0 = 5 minutes, 10.5 = 10 minutes 30 seconds)"
    )


class ProductProduct(models.Model):
    _inherit = 'product.product'

    prepair_time_minutes = fields.Float(
        related='product_tmpl_id.prepair_time_minutes',
        string='Preparation Time (minutes)',
        readonly=False,
        store=True
    )