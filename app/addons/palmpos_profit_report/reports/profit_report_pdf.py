# -*- coding: utf-8 -*-

from odoo import models


class ProfitReportPdf(models.AbstractModel):
    _name = 'report.palmpos_profit_report.report_profit_template'
    _description = 'Profit Report PDF'

    def _get_report_values(self, docids, data=None):
        docs = self.env['pos.profit.report'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'pos.profit.report',
            'docs': docs,
            'data': data,
        }
