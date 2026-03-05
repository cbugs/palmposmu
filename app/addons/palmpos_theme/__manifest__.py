{
    'name': 'PalmPOS Theme',
    'version': '19.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Custom CSS styles for PalmPOS',
    'depends': ['web', 'point_of_sale'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'palmpos_theme/static/src/css/palmpos.css',
        ],
        'web.assets_frontend': [
            'palmpos_theme/static/src/css/palmpos.css',
            'palmpos_theme/static/src/js/install_scoped_app.js',
            'palmpos_theme/static/src/xml/install_scoped_app.xml',
        ],
        'point_of_sale._assets_pos': [
            'palmpos_theme/static/src/css/pos_branding.css',
            'palmpos_theme/static/src/js/replace_branding.js',
            'palmpos_theme/static/src/xml/pos_branding.xml',
        ],        
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
