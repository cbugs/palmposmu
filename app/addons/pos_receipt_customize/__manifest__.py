{
    'name': 'POS Receipt Customize',
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Remove logo and Powered by Odoo label from POS receipts, set PDF filename to receipt ID, send receipt via WhatsApp',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_receipt_customize/static/src/css/receipt.css',
            'pos_receipt_customize/static/src/js/receipt_filename.js',
            'pos_receipt_customize/static/src/js/whatsapp_button.js',
            'pos_receipt_customize/static/src/xml/receipt_footer.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
