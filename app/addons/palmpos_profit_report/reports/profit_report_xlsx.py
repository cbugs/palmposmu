# -*- coding: utf-8 -*-

import io

import xlsxwriter
from odoo import http
from odoo.http import content_disposition, request


class ProfitReportController(http.Controller):

    @http.route('/pos/profit/report/excel/<int:report_id>', type='http', auth='user')
    def download_profit_report_excel(self, report_id, **kwargs):
        """Download profit report as Excel file"""
        report = request.env['pos.profit.report'].browse(report_id)
        
        if not report.exists():
            return request.not_found()
        
        # Create Excel file in memory
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Profit Report')
        
        # Define formats
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#4CAF50',
            'color': 'white',
            'align': 'center',
            'valign': 'vcenter',
            'border': 1
        })
        
        money_format = workbook.add_format({'num_format': '$#,##0.00'})
        percent_format = workbook.add_format({'num_format': '0.00%'})
        number_format = workbook.add_format({'num_format': '#,##0.00'})
        
        # Write title
        worksheet.merge_range('A1:H1', f'PalmPOS Profit Report - {dict(report._fields["report_type"].selection).get(report.report_type)}', 
                             workbook.add_format({'bold': True, 'font_size': 16, 'align': 'center'}))
        
        # Write date range
        worksheet.merge_range('A2:H2', f'From: {report.date_from} To: {report.date_to}', 
                             workbook.add_format({'align': 'center'}))
        
        # Write headers
        headers = ['Name', 'Quantity', 'Sales', 'Cost', 'Tax', 'Discount', 'Profit', 'Margin %']
        for col, header in enumerate(headers):
            worksheet.write(3, col, header, header_format)
        
        # Write data
        row = 4
        for line in report.line_ids:
            worksheet.write(row, 0, line.name)
            worksheet.write(row, 1, line.quantity, number_format)
            worksheet.write(row, 2, line.sales_amount, money_format)
            worksheet.write(row, 3, line.cost_amount, money_format)
            worksheet.write(row, 4, line.tax_amount, money_format)
            worksheet.write(row, 5, line.discount_amount, money_format)
            worksheet.write(row, 6, line.profit_amount, money_format)
            worksheet.write(row, 7, line.profit_margin / 100, percent_format)
            row += 1
        
        # Write totals
        row += 1
        total_format = workbook.add_format({'bold': True, 'bg_color': '#E0E0E0', 'border': 1})
        total_money_format = workbook.add_format({'bold': True, 'num_format': '$#,##0.00', 'bg_color': '#E0E0E0', 'border': 1})
        total_percent_format = workbook.add_format({'bold': True, 'num_format': '0.00%', 'bg_color': '#E0E0E0', 'border': 1})
        
        total_qty = sum(report.line_ids.mapped('quantity'))
        
        worksheet.write(row, 0, 'TOTAL', total_format)
        worksheet.write(row, 1, total_qty, total_money_format)
        worksheet.write(row, 2, report.total_sales, total_money_format)
        worksheet.write(row, 3, report.total_cost, total_money_format)
        worksheet.write(row, 4, report.total_tax, total_money_format)
        worksheet.write(row, 5, report.total_discount, total_money_format)
        worksheet.write(row, 6, report.total_profit, total_money_format)
        worksheet.write(row, 7, report.profit_margin / 100, total_percent_format)
        
        # Adjust column widths
        worksheet.set_column('A:A', 30)
        worksheet.set_column('B:H', 15)
        
        workbook.close()
        output.seek(0)
        
        filename = f'profit_report_{report.report_type}_{report.date_from}_{report.date_to}.xlsx'
        
        return request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', content_disposition(filename))
            ]
        )
