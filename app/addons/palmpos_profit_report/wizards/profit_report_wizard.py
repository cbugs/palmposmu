# -*- coding: utf-8 -*-

from odoo import fields, models


class ProfitReportWizard(models.TransientModel):
    _inherit = 'pos.profit.report'
    _name = 'profit.report.wizard'
    _description = 'Profit Report Wizard'
