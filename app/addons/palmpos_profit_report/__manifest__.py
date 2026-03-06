# -*- coding: utf-8 -*-
{
    'name': 'PalmPOS Profit & Loss Report',
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Generate profit reports by product, customer, and date range with PDF/Excel export',
    'description': """
        POS Profit & Loss Reporting
        ============================
        
        Features:
        ---------
        * Profit report by product
        * Profit report by customer
        * Profit report by date range
        * Export to PDF and Excel
        * Shows sale price, cost, tax, discount, and profit
        * Clean and professional reports
        * Filter by session, date range, product category, etc.
    """,
    'depends': ['point_of_sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/profit_report_wizard_views.xml',
        'views/pos_profit_report_views.xml',
        'reports/profit_report_template.xml',
        'views/sales_details_template.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
