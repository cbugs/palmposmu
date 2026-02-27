{
    'name': 'PalmPOS Title',
    'version': '19.0.1.0.0',
    'category': 'Web',
    'summary': 'Sets the browser title to PalmPOS',
    'description': 'Changes the browser tab title to PalmPOS',
    'depends': ['web'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'palmpos_title/static/src/js/title.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
