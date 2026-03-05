{
    'name': 'POS Receipt Customize',
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Remove logo and Powered by Odoo label from POS receipts, set PDF filename to receipt ID',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_receipt_customize/static/src/css/receipt.css',
            'pos_receipt_customize/static/src/js/receipt_filename.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
