{
    'name': 'PalmPOS Title',
    'version': '19.0.1.0.0',
    'category': 'Web',
    'summary': 'Sets the browser title to PalmPOS',
    'description': 'Changes the browser tab title to PalmPOS',
    'depends': ['web', 'point_of_sale'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'palmpos_title/static/src/js/title.js',
        ],
        'point_of_sale._assets_pos': [
            'palmpos_title/static/src/js/pos_title.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
