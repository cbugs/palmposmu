# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import api, fields, models


class PosProfitReport(models.TransientModel):
    _name = 'pos.profit.report'
    _description = 'POS Profit Report Data'

    name = fields.Char(string='Report Name', compute='_compute_name', store=True)
    
    report_type = fields.Selection([
        ('product', 'By Product'),
        ('customer', 'By Customer'),
        ('date', 'By Date Range'),
    ], string='Report Type', required=True, default='product')
    
    date_from = fields.Date(string='Date From', required=True, default=fields.Date.today)
    date_to = fields.Date(string='Date To', required=True, default=fields.Date.today)
    
    session_ids = fields.Many2many('pos.session', string='POS Sessions')
    product_ids = fields.Many2many('product.product', string='Products')
    categ_ids = fields.Many2many('product.category', string='Product Categories')
    partner_ids = fields.Many2many('res.partner', string='Customers')
    
    line_ids = fields.One2many('pos.profit.report.line', 'report_id', string='Report Lines')
    
    # Currency for monetary fields
    currency_id = fields.Many2one('res.currency', string='Currency', 
                                   default=lambda self: self.env.company.currency_id)
    
    # Summary fields
    total_sales = fields.Float(string='Total Sales', compute='_compute_totals', store=True)
    total_cost = fields.Float(string='Total Cost', compute='_compute_totals', store=True)
    total_tax = fields.Float(string='Total Tax', compute='_compute_totals', store=True)
    total_discount = fields.Float(string='Total Discount', compute='_compute_totals', store=True)
    total_profit = fields.Float(string='Total Profit', compute='_compute_totals', store=True)
    profit_margin = fields.Float(string='Profit Margin %', compute='_compute_totals', store=True)

    @api.depends('report_type', 'date_from', 'date_to')
    def _compute_name(self):
        for report in self:
            type_name = dict(report._fields['report_type'].selection).get(report.report_type, 'Report')
            report.name = f'{type_name} - {report.date_from} to {report.date_to}'

    @api.depends('line_ids.sales_amount', 'line_ids.cost_amount', 'line_ids.tax_amount', 
                 'line_ids.discount_amount', 'line_ids.profit_amount')
    def _compute_totals(self):
        for report in self:
            report.total_sales = sum(report.line_ids.mapped('sales_amount'))
            report.total_cost = sum(report.line_ids.mapped('cost_amount'))
            report.total_tax = sum(report.line_ids.mapped('tax_amount'))
            report.total_discount = sum(report.line_ids.mapped('discount_amount'))
            report.total_profit = sum(report.line_ids.mapped('profit_amount'))
            report.profit_margin = (report.total_profit / report.total_sales * 100) if report.total_sales else 0

    def action_generate_report(self):
        """Generate the profit report based on selected criteria"""
        self.ensure_one()
        
        # Create a new report to avoid constraint issues with transient model cleanup
        report = self.env['pos.profit.report'].create({
            'report_type': self.report_type,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'session_ids': [(6, 0, self.session_ids.ids)],
            'product_ids': [(6, 0, self.product_ids.ids)],
            'categ_ids': [(6, 0, self.categ_ids.ids)],
            'partner_ids': [(6, 0, self.partner_ids.ids)],
        })
        
        # Get POS orders in date range
        domain = [
            ('date_order', '>=', report.date_from),
            ('date_order', '<=', report.date_to),
            ('state', 'in', ['paid', 'done', 'invoiced']),
        ]
        
        if report.session_ids:
            domain.append(('session_id', 'in', report.session_ids.ids))
        
        if report.partner_ids:
            domain.append(('partner_id', 'in', report.partner_ids.ids))
        
        orders = self.env['pos.order'].search(domain)
        
        # Generate report based on type
        if report.report_type == 'product':
            report._generate_product_report(orders)
        elif report.report_type == 'customer':
            report._generate_customer_report(orders)
        elif report.report_type == 'date':
            report._generate_date_report(orders)
        
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'pos.profit.report',
            'view_mode': 'form',
            'res_id': report.id,
            'target': 'current',
        }

    def _generate_product_report(self, orders):
        """Generate profit report grouped by product"""
        product_data = {}
        
        for order in orders:
            for line in order.lines:
                product = line.product_id
                
                # Filter by products if specified
                if self.product_ids and product not in self.product_ids:
                    continue
                
                # Filter by categories if specified
                if self.categ_ids and product.categ_id not in self.categ_ids:
                    continue
                
                if product.id not in product_data:
                    product_data[product.id] = {
                        'product_id': product.id,
                        'name': product.display_name,
                        'quantity': 0,
                        'sales_amount': 0,
                        'cost_amount': 0,
                        'tax_amount': 0,
                        'discount_amount': 0,
                    }
                
                # Calculate amounts
                qty = line.qty
                price_subtotal_incl = line.price_subtotal_incl
                price_subtotal = line.price_subtotal
                tax_amount = price_subtotal_incl - price_subtotal
                discount_amount = (line.price_unit * qty) - price_subtotal
                
                # Get cost - use standard_price from product
                cost = product.standard_price * qty
                
                product_data[product.id]['quantity'] += qty
                product_data[product.id]['sales_amount'] += price_subtotal_incl
                product_data[product.id]['cost_amount'] += cost
                product_data[product.id]['tax_amount'] += tax_amount
                product_data[product.id]['discount_amount'] += discount_amount
        
        # Create report lines
        for data in product_data.values():
            self.env['pos.profit.report.line'].create({
                'report_id': self.id,
                'product_id': data['product_id'],
                'name': data['name'],
                'quantity': data['quantity'],
                'sales_amount': data['sales_amount'],
                'cost_amount': data['cost_amount'],
                'tax_amount': data['tax_amount'],
                'discount_amount': data['discount_amount'],
            })

    def _generate_customer_report(self, orders):
        """Generate profit report grouped by customer"""
        customer_data = {}
        
        for order in orders:
            if order.partner_id:
                partner_id = order.partner_id.id
                partner_name = order.partner_id.name
            else:
                # For orders without a customer, use a consistent key
                partner_id = 0
                partner_name = 'Walk-in Customer'
            
            if partner_id not in customer_data:
                customer_data[partner_id] = {
                    'partner_id': partner_id,
                    'name': partner_name,
                    'quantity': 0,
                    'sales_amount': 0,
                    'cost_amount': 0,
                    'tax_amount': 0,
                    'discount_amount': 0,
                }
            
            for line in order.lines:
                # Calculate amounts
                qty = line.qty
                price_subtotal_incl = line.price_subtotal_incl
                price_subtotal = line.price_subtotal
                tax_amount = price_subtotal_incl - price_subtotal
                discount_amount = (line.price_unit * qty) - price_subtotal
                cost = line.product_id.standard_price * qty
                
                customer_data[partner_id]['quantity'] += qty
                customer_data[partner_id]['sales_amount'] += price_subtotal_incl
                customer_data[partner_id]['cost_amount'] += cost
                customer_data[partner_id]['tax_amount'] += tax_amount
                customer_data[partner_id]['discount_amount'] += discount_amount
        
        # Create report lines
        for data in customer_data.values():
            self.env['pos.profit.report.line'].create({
                'report_id': self.id,
                'partner_id': data['partner_id'],
                'name': data['name'],
                'quantity': data['quantity'],
                'sales_amount': data['sales_amount'],
                'cost_amount': data['cost_amount'],
                'tax_amount': data['tax_amount'],
                'discount_amount': data['discount_amount'],
            })

    def _generate_date_report(self, orders):
        """Generate profit report grouped by date"""
        date_data = {}
        
        for order in orders:
            date = order.date_order.date()
            date_str = date.strftime('%Y-%m-%d')
            
            if date_str not in date_data:
                date_data[date_str] = {
                    'date': date,
                    'name': date.strftime('%B %d, %Y'),
                    'quantity': 0,
                    'sales_amount': 0,
                    'cost_amount': 0,
                    'tax_amount': 0,
                    'discount_amount': 0,
                }
            
            for line in order.lines:
                # Calculate amounts
                qty = line.qty
                price_subtotal_incl = line.price_subtotal_incl
                price_subtotal = line.price_subtotal
                tax_amount = price_subtotal_incl - price_subtotal
                discount_amount = (line.price_unit * qty) - price_subtotal
                cost = line.product_id.standard_price * qty
                
                date_data[date_str]['quantity'] += qty
                date_data[date_str]['sales_amount'] += price_subtotal_incl
                date_data[date_str]['cost_amount'] += cost
                date_data[date_str]['tax_amount'] += tax_amount
                date_data[date_str]['discount_amount'] += discount_amount
        
        # Create report lines
        for data in date_data.values():
            self.env['pos.profit.report.line'].create({
                'report_id': self.id,
                'date': data['date'],
                'name': data['name'],
                'quantity': data['quantity'],
                'sales_amount': data['sales_amount'],
                'cost_amount': data['cost_amount'],
                'tax_amount': data['tax_amount'],
                'discount_amount': data['discount_amount'],
            })

    def action_export_excel(self):
        """Export report to Excel"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': f'/pos/profit/report/excel/{self.id}',
            'target': 'new',
        }

    def action_print_pdf(self):
        """Print report as PDF"""
        self.ensure_one()
        return self.env.ref('palmpos_profit_report.action_report_pos_profit').report_action(self)


class PosProfitReportLine(models.TransientModel):
    _name = 'pos.profit.report.line'
    _description = 'POS Profit Report Line'
    _order = 'sales_amount desc'

    report_id = fields.Many2one('pos.profit.report', string='Report', required=True, ondelete='cascade')
    
    # Group by fields
    product_id = fields.Many2one('product.product', string='Product')
    partner_id = fields.Many2one('res.partner', string='Customer')
    date = fields.Date(string='Date')
    
    name = fields.Char(string='Name', required=True)
    quantity = fields.Float(string='Quantity')
    
    currency_id = fields.Many2one('res.currency', string='Currency', related='report_id.currency_id', store=True)
    
    sales_amount = fields.Float(string='Sales')
    cost_amount = fields.Float(string='Cost')
    tax_amount = fields.Float(string='Tax')
    discount_amount = fields.Float(string='Discount')
    profit_amount = fields.Float(string='Profit', compute='_compute_profit', store=True)
    profit_margin = fields.Float(string='Margin %', compute='_compute_profit', store=True)

    @api.depends('sales_amount', 'cost_amount')
    def _compute_profit(self):
        for line in self:
            line.profit_amount = line.sales_amount - line.cost_amount
            line.profit_margin = (line.profit_amount / line.sales_amount * 100) if line.sales_amount else 0
